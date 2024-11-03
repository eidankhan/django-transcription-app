# Django Transcription App

This is a Django-based web application that provides audio transcription services using OpenAI's Whisper model. Users can upload audio files, and the app generates text transcriptions. The application offers a user-friendly interface with real-time audio playback and synchronized word-by-word highlighting, enhancing the transcription review experience.

## Features

- **Audio File Upload**: Users can upload audio files directly on the web interface.
- **Transcription with Timestamps**: he app transcribes audio using the Whisper model and includes word-by-word timestamps.
- **Real-Time Audio Playback with Word Highlighting**: As the audio plays, each word in the transcription is highlighted in sync, helping users evaluate transcription accuracy.
- **Responsive UI**: Clean and responsive user interface with Bootstrap and Materialize, providing an intuitive user experience.

## Planned Features

- **Summarization**: Add a feature to generate summaries of transcribed text.
- **User Authentication**: Allow users to register and manage their transcription files.
- **File History**: Store transcription files and history for registered users..
- **Enhanced Accuracy Controls**: Allow users to select models optimized for either speed or accuracy based on audio quality.

## Usage
- **Upload an Audio File**: Select an audio file and choose the audio quality type.
- **Transcribe**: Click the "Transcribe" button to start transcription.
- **Audio Playback with Highlighted Transcription**: The app will display an audio player along with the transcribed text. Each word is highlighted in sync with audio playback, making it easy to verify transcription accuracy.

## Future Improvements
- **Enhanced UI with Themes**: Provide a more customizable and visually appealing interface.
- **Advanced Settings**: Options for choosing different Whisper models based on audio quality (e.g., noisy vs. clear).
- **Performance Optimization**: Further reduce transcription time and improve overall app performance.

## Requirements

- **Python 3.9.9**
- **Django**: A web framework used to create the project.
- **Whisper**: OpenAI's Whisper library, used for audio transcription.
- **FFmpeg**: Required by Whisper to process audio files.
