# transcription/services/transcription_service.py

import whisper

# Dictionary mapping model names to their loaded Whisper models based on official availability
model_dict = {
    "tiny": whisper.load_model("tiny"),          # Multilingual
    # "tiny.en": whisper.load_model("tiny.en"),    # English-only
    "base": whisper.load_model("base"),          # Multilingual
    # "base.en": whisper.load_model("base.en"),    # English-only
    "small": whisper.load_model("small"),        # Multilingual
    # "small.en": whisper.load_model("small.en"),  # English-only
    "medium": whisper.load_model("medium"),      # Multilingual
    # "medium.en": whisper.load_model("medium.en"),# English-only
    # "large": whisper.load_model("large"),        # Multilingual only
    "turbo": whisper.load_model("turbo")         # Multilingual optimized for inference speed
}

def transcribe_audio_with_model(model_name, audio_path):
    """Transcribe the audio file using the specified model."""
    if model_name not in model_dict:
        raise ValueError(f"Model '{model_name}' is not available. Choose from: {list(model_dict.keys())}")

    model = model_dict[model_name]  # Retrieve the chosen model from the dictionary
    result = model.transcribe(audio_path)
    return result["text"]
