# Install necessary libraries
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import whisper
import tempfile
import os
from .services import transcription_service

model_name = "tiny"  # Choose from "tiny", "base", "small", "medium", "large", "turbo" etc.


# Create your views here.

def index(request):
    return render(request, 'transcription/index.html')
def transcribe(request):
    # Check if the request is AJAX by looking at the HTTP header
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        audio_file = request.FILES['audio_file']

        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            for chunk in audio_file.chunks():
                tmp_file.write(chunk)
            tmp_file_path = tmp_file.name

        # Transcribe the audio file
        try:
            transcription = transcription_service.transcribe_audio_with_model(model_name, tmp_file_path)
            return JsonResponse({"transcription": transcription})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        finally:
            os.remove(tmp_file_path)  # Clean up temporary file

    return JsonResponse({"error": "Invalid request"}, status=400)
