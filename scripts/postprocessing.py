import re

def add_punctuation(transcription):
    """
    Menambahkan tanda baca ke hasil transkripsi yang masih berupa teks polos.
    
    Args:
        transcription (str): Teks transkripsi tanpa tanda baca.
    
    Returns:
        transcription_with_punctuation (str): Teks transkripsi dengan tanda baca yang ditambahkan.
    """
    # Menambahkan titik pada akhir kalimat sederhana
    transcription_with_punctuation = re.sub(r'([a-z])(\s|$)', r'\1. ', transcription)
    return transcription_with_punctuation

def correct_spelling(transcription):
    """
    Koreksi otomatis pada teks transkripsi (contoh sederhana).
    
    Args:
        transcription (str): Teks transkripsi.
    
    Returns:
        corrected_transcription (str): Teks transkripsi setelah koreksi otomatis.
    """
    # Contoh koreksi otomatis menggunakan dictionary sederhana (dapat diperluas)
    corrections = {
        "teh": "the",
        "exmaple": "example"
    }
    
    words = transcription.split()
    corrected_words = [corrections.get(word, word) for word in words]
    corrected_transcription = ' '.join(corrected_words)
    
    return corrected_transcription
