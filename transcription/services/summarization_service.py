# transcription/services/summarization_service.py

from transformers import pipeline

# Load the BART summarization model and tokenizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text, max_length=150, min_length=30, do_sample=False):
    """
    Generate a summary for the given text.

    Parameters:
    - text (str): The input text to summarize.
    - max_length (int): Maximum length of the summary.
    - min_length (int): Minimum length of the summary.
    - do_sample (bool): Whether to use sampling; useful for creative summaries.

    Returns:
    - str: The generated summary.
    """
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
    return summary[0]["summary_text"]
