# Django Transcription App

This is a Django-based web application that provides audio transcription services using OpenAI's Whisper model. Users can upload audio files, and the app generates text transcriptions. This is an MVP (Minimum Viable Product) version, with additional features planned for future development.

## Features

- **Audio File Upload**: Users can upload audio files directly on the web interface.
- **Transcription**: Once the file is uploaded, the app transcribes the audio using the locally installed Whisper model.
- **Simple UI**: Basic file upload form to keep the initial version straightforward and user-friendly.

## Planned Features

- **Summarization**: Add a feature to generate summaries of transcribed text.
- **User Authentication**: Allow users to register and manage their transcription files.
- **Enhanced UI**: Improve the user interface for a better user experience.
- **File History**: Store transcription files and history for registered users.

## Requirements

- **Python 3.9.9**
- **Django**: A web framework used to create the project.
- **Whisper**: OpenAI's Whisper library, used for audio transcription.
- **FFmpeg**: Required by Whisper to process audio files.
