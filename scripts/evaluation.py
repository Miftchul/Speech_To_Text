from jiwer import wer

def evaluate_transcription(reference, hypothesis):
    """
    Menghitung Word Error Rate (WER) antara transkripsi referensi dan hasil transkripsi model.
    
    Args:
        reference (str): Transkripsi referensi yang benar.
        hypothesis (str): Transkripsi yang dihasilkan oleh model.
    
    Returns:
        error_rate (float): Nilai WER antara referensi dan hipotesis.
    """
    # Normalisasi teks untuk WER (misalnya huruf kecil semua)
    reference = reference.lower()
    hypothesis = hypothesis.lower()
    
    # Menghitung WER
    error_rate = wer(reference, hypothesis)
    return error_rate
