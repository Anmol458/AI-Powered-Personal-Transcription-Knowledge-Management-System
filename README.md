# AI-Powered Personal Transcription & Knowledge Management System

A locally hosted personal transcription and knowledge-management pipeline that converts spoken conversations into structured knowledge.

## Overview

This project combines local speech recognition, automated text organization and a personal knowledge base into a single workflow.

The system captures audio through a laptop microphone(currently, a portable recorder is under development), records the conversation as WAV audio, uses a locally running Whisper-based speech-to-text model to generate Markdown transcripts, stores the transcripts in an Obsidian knowledge vault and uses a locally hosted Ollama LLM agent (Gemma-4e - 64K) to identify topics and organize information into structured notes.

## System Architecture

Laptop Microphone -> Audio Capture -> WAV Recording -> Local Whisper Model -> Markdown Transcript -> Obsidian Vault -> Local Ollama LLM Agent -> Topic Extraction & Organization -> Structured Personal Knowledge Base


## Technologies Used

- Python
- faster-whisper / Whisper
- CUDA
- Ollama
- Obsidian
- sounddevice
- WAV / PCM audio
- Markdown

## Pipeline

1. Audio Capture

The system captures audio through the laptop microphone and records speech into WAV files.

The audio recording pipeline is designed to separate real-time audio capture from the slower transcription process.

2. Local Speech-to-Text

The recorded WAV files are processed using a locally running Whisper-based model.

The generated transcription is stored as Markdown.

Example:

# Daily Conversation — 30 September 2026

## 14:32:15

Today I worked on the transcription pipeline...

3. Obsidian Knowledge Vault

The generated Markdown files are stored in an Obsidian vault.

This allows the transcripts to become part of a searchable personal knowledge base.

4. Local LLM Organization

A locally hosted Ollama LLM agent processes the raw transcripts. The Gemma-4e model is running on Hermes agent which allows it to remember and evolve with the user inputs. 

The agent identifies topics and organizes relevant information into structured knowledge notes.

The project is designed around local processing, aiming to build private and secure day-to-day transcribers for individuals.


## Hardware Extension

A future extension of the project is a standalone ESP32-based recording device with a dedicated microphone.

The intended architecture is:

ESP32 + Microphone -> WAV Audio -> Laptop -> Local Whisper -> Obsidian -> Ollama Knowledge Organization

The current implemented transcription pipeline uses the laptop microphone.

## Demo

Screenshots and a demonstration video are included in the screenshots/ and demo/ directories.

## Author

Anmolabjot Singh

Electronics and Communication Engineering
