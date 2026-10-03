from faster_whisper import WhisperModel
from datetime import datetime

model = WhisperModel(
    "base",
    device="cuda",
    compute_type="float16"
)

segments, info = model.transcribe("test.wav")

today = datetime.now().strftime("%d %B %Y")

with open("daily.md", "w", encoding="utf-8") as file:
    file.write(f"# Daily Conversation — {today}\n\n")

    for segment in segments:
        timestamp = datetime.now().strftime("%H:%M:%S")

        file.write(f"## {timestamp}\n\n")
        file.write(f"{segment.text.strip()}\n\n")

print("Transcript saved to daily.md")
