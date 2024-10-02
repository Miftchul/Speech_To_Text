from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch

# Fungsi untuk memuat model berdasarkan bahasa yang dipilih
def load_model(language):
    """
    Memuat model Wav2Vec2 yang sesuai dengan bahasa yang dipilih.
    
    Args:
        language (str): Kode bahasa yang dipilih ('id', 'en', 'zh').
        
    Returns:
        processor, model: Processor dan model yang sesuai dengan bahasa.
    """
    if language == 'id':
        # Bahasa Indonesia
        processor = Wav2Vec2Processor.from_pretrained("indonesian-nlp/wav2vec2-large-xlsr-indonesian")
        model = Wav2Vec2ForCTC.from_pretrained("indonesian-nlp/wav2vec2-large-xlsr-indonesian")
    elif language == 'zh':
        # Bahasa China
        processor = Wav2Vec2Processor.from_pretrained("jonatasgrosman/wav2vec2-large-xlsr-53-chinese-zh-cn")
        model = Wav2Vec2ForCTC.from_pretrained("jonatasgrosman/wav2vec2-large-xlsr-53-chinese-zh-cn")
    else:
        # Default ke Bahasa Inggris
        processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
        model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")
    
    return processor, model

# Fungsi untuk transkripsi audio berdasarkan bahasa
def transcribe_audio_with_language(audio, sample_rate, language):
    """
    Melakukan inferensi pada data audio dan mengembalikan teks transkripsi.
    
    Args:
        audio (numpy.ndarray): Data audio input.
        sample_rate (int): Sample rate audio input.
        language (str): Kode bahasa ('id' untuk Indonesia, 'en' untuk Inggris, 'zh' untuk China).
    
    Returns:
        transcription (str): Hasil transkripsi dari audio.
    """
    # Memuat model dan processor sesuai bahasa yang dipilih
    processor, model = load_model(language)
    
    # Mengubah audio menjadi input tensor yang dapat diterima oleh model
    input_values = processor(audio, sampling_rate=sample_rate, return_tensors="pt").input_values
    
    # Forward pass pada model untuk mendapatkan logits
    with torch.no_grad():
        logits = model(input_values).logits
    
    # Mengambil prediksi dengan probabilitas tertinggi (argmax)
    predicted_ids = torch.argmax(logits, dim=-1)
    
    # Meng-decode prediksi ke dalam teks
    transcription = processor.decode(predicted_ids[0])
    return transcription
