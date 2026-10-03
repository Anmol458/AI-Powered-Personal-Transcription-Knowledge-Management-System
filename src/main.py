import sounddevice as sd
import queue
import numpy as np
import time
from datetime import datetime
from faster_whisper import WhisperModel
from pathlib import Path
import wave
import threading
import shutil


# ============================================================
# CONFIGURATION
# ============================================================

SAMPLE_RATE = 16000
CHANNELS = 1
CHUNK_DURATION = 0.5
DEVICE = 1

CHUNK_SIZE = int(SAMPLE_RATE * CHUNK_DURATION)

THRESHOLD = 700
SILENCE_DURATION = 10


# ============================================================
# FOLDERS
# ============================================================

INBOX = Path("recordings/inbox")
PROCESSED = Path("recordings/processed")
FAILED = Path("recordings/failed")

INBOX.mkdir(parents=True, exist_ok=True)
PROCESSED.mkdir(parents=True, exist_ok=True)
FAILED.mkdir(parents=True, exist_ok=True)

NOTES = Path("Transcribed_Notes/RAW")
NOTES.mkdir(parents=True, exist_ok=True)


# ============================================================
# AUDIO QUEUE
# ============================================================

audio_queue = queue.Queue()


# ============================================================
# MICROPHONE CALLBACK
# ============================================================

def audio_callback(indata, frames, time_info, status):

    if status:
        print("Audio status:", status)

    audio_queue.put(indata.copy())


# ============================================================
# SAVE SPEECH SEGMENT
# ============================================================

def save_audio(chunks, start_time):

    audio = np.concatenate(chunks)

    timestamp = start_time.strftime(
        "%Y%m%d_%H%M%S_%f"
    )

    filename = INBOX / f"speech_{timestamp}.wav"

    temp_filename = INBOX / f"speech_{timestamp}.tmp.wav"

    with wave.open(str(temp_filename), "wb") as wav_file:

        wav_file.setnchannels(CHANNELS)

        wav_file.setsampwidth(2)

        wav_file.setframerate(SAMPLE_RATE)

        wav_file.writeframes(
            audio.tobytes()
        )

    # The file becomes visible to the transcription
    # worker only after the WAV is completely written.
    temp_filename.rename(filename)

    return filename


# ============================================================
# TRANSCRIBER WORKER
# ============================================================

def transcription_worker():

    print("Loading Whisper in background...")

    model = WhisperModel(
        "base",
        device="cuda",
        compute_type="float16"
    )

    print("Whisper loaded.")
    print("Background transcription worker ready.")

    while True:

        files = sorted(
            INBOX.glob("*.wav")
        )

        if not files:

            time.sleep(1)

            continue

        audio_file = files[0]

        print(
            f"\n[Whisper] Processing: "
            f"{audio_file.name}"
        )

        try:

            segments, info = model.transcribe(
                str(audio_file)
            )

            text_parts = []

            for segment in segments:

                text_parts.append(
                    segment.text.strip()
                )

            text = " ".join(text_parts).strip()

            if text:

                write_to_markdown(
                    text,
                    audio_file
                )

                print(
                    f"[Whisper] Transcript: {text}"
                )

                print(
                    "[Whisper] Saved to daily.md"
                )

            else:

                print(
                    "[Whisper] No speech detected."
                )

            shutil.move(
                str(audio_file),
                PROCESSED / audio_file.name
            )

        except Exception as error:

            print(
                f"[Whisper] ERROR: {error}"
            )

            shutil.move(
                str(audio_file),
                FAILED / audio_file.name
            )


# ============================================================
# MARKDOWN WRITER
# ============================================================

def write_to_markdown(text, audio_file):

    # Extract recording time from the WAV filename.
    #
    # speech_20260831_012013_123456.wav
    #
    # → 2026-08-31 01:20:13

    filename = audio_file.stem

    timestamp_string = filename.replace(
        "speech_",
        ""
    )

    recording_time = datetime.strptime(
        timestamp_string,
        "%Y%m%d_%H%M%S_%f"
    )

    # Date used for the filename
    date_filename = recording_time.strftime(
        "%Y-%m-%d"
    )

    # Human-readable date used inside Markdown
    date_string = recording_time.strftime(
        "%d %B %Y"
    )

    # Time of the actual conversation
    time_string = recording_time.strftime(
        "%H:%M:%S"
    )

    # Create today's Markdown file
    markdown_file = NOTES / f"{date_filename}.md"

    # Create the daily heading only if this is a new file
    if not markdown_file.exists():

        with markdown_file.open(
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                f"# Daily Conversation — {date_string}\n\n"
            )

    # Append this conversation to today's file
    with markdown_file.open(
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"## {time_string}\n\n"
        )

        file.write(
            f"{text}\n\n"
        )

# ============================================================
# START BACKGROUND WORKER
# ============================================================

worker = threading.Thread(
    target=transcription_worker,
    daemon=True
)

worker.start()


# ============================================================
# START MICROPHONE
# ============================================================

print()
print("Starting microphone...")
print("Speak normally.")
print("Press Ctrl+C to stop.")
print()


speaking = False
speech_buffer = []

silence_start = None
speech_start_time = None


with sd.InputStream(
    samplerate=SAMPLE_RATE,
    channels=CHANNELS,
    dtype="int16",
    device=DEVICE,
    blocksize=CHUNK_SIZE,
    callback=audio_callback
):

    try:

        while True:

            audio_chunk = audio_queue.get()

            volume = np.sqrt(
                np.mean(
                    audio_chunk.astype(
                        np.float32
                    ) ** 2
                )
            )


            # ==================================================
            # SPEECH
            # ==================================================

            if volume > THRESHOLD:

                if not speaking:

                    print(
                        "\n>>> SPEECH STARTED"
                    )

                    speaking = True

                    speech_buffer = []

                    speech_start_time = (
                        datetime.now()
                    )

                speech_buffer.append(
                    audio_chunk
                )

                silence_start = None

                print(
                    f"Speech: {volume:.0f}"
                )


            # ==================================================
            # SILENCE
            # ==================================================

            else:

                if speaking:

                    speech_buffer.append(
                        audio_chunk
                    )

                    if silence_start is None:

                        silence_start = (
                            time.time()
                        )

                    silence_elapsed = (
                        time.time()
                        - silence_start
                    )

                    print(
                        f"Silence: "
                        f"{volume:.0f} "
                        f"({silence_elapsed:.1f}s)"
                    )


                    # ==========================================
                    # SPEECH ENDED
                    # ==========================================

                    if (
                        silence_elapsed
                        >= SILENCE_DURATION
                    ):

                        print(
                            ">>> SPEECH ENDED"
                        )

                        audio_file = save_audio(
                            speech_buffer,
                            speech_start_time
                        )

                        print(
                            f">>> Queued: "
                            f"{audio_file.name}"
                        )

                        # Reset recorder immediately.
                        #
                        # IMPORTANT:
                        # We do NOT wait for Whisper.

                        speaking = False

                        speech_buffer = []

                        silence_start = None

                        speech_start_time = None


    except KeyboardInterrupt:

        print("\nStopped.")
