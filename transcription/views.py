# Install necessary libraries
from django.shortcuts import render
from django.http import HttpResponse
import whisper
import tempfile
import os


# Create your views here.

def index(request):
    return render(request, 'transcription/index.html')

def transcribe(request):
    if request.method == 'POST':
        audio_file = request.FILES['audio_file']

        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            for chunk in audio_file.chunks():
                tmp_file.write(chunk)
            tmp_file_path = tmp_file.name

        # Load the Whisper model
        model = whisper.load_model("base")  # Use "tiny", "base", "small", "medium", or "large" based on performance requirements

        # Transcribe the audio file
        try:
            result = model.transcribe(tmp_file_path)
            transcription_text = result["text"]
            return HttpResponse(f"Transcription: {transcription_text}")
        except Exception as e:
            return HttpResponse(f"Error during transcription: {e}")
        finally:
            # Clean up temporary file
            os.remove(tmp_file_path)

    return HttpResponse("Please upload an audio file.")