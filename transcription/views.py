# Install necessary libraries
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import whisper
import tempfile
import os


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

        # Load Whisper model
        model = whisper.load_model("base")

        # Transcribe the audio file
        try:
            result = model.transcribe(tmp_file_path)
            transcription_text = result["text"]
            return JsonResponse({"transcription": transcription_text})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        finally:
            os.remove(tmp_file_path)  # Clean up temporary file

    return JsonResponse({"error": "Invalid request"}, status=400)
