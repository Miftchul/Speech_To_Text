import sounddevice as sd
import numpy as np
from scripts.model import transcribe_audio_with_language
from scripts.postprocessing import add_punctuation

# Fungsi untuk merekam audio dari mikrofon
def record_audio(duration=5, sample_rate=16000):
    """
    Merekam audio dari mikrofon.
    
    Args:
        duration (int): Durasi rekaman dalam detik.
        sample_rate (int): Sample rate untuk audio (default 16kHz).
    
    Returns:
        numpy.ndarray: Data audio yang direkam.
    """
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()  # Tunggu hingga rekaman selesai
    audio = np.squeeze(audio)  # Menghapus dimensi berlebih
    return audio

# Fungsi untuk memilih bahasa
def choose_language():
    """
    Menampilkan menu pilihan bahasa dan mengembalikan bahasa yang dipilih.
    
    Returns:
        str: Kode bahasa yang dipilih ('id' untuk Indonesia, 'en' untuk Inggris, 'zh' untuk China).
    """
    print("Bahasa apa yang Anda gunakan?")
    print("1. Bahasa Indonesia")
    print("2. Bahasa Inggris")
    print("3. Bahasa China")
    
    choice = input("Masukkan pilihan (1/2/3): ")
    
    if choice == '1':
        return 'id'  # Bahasa Indonesia
    elif choice == '2':
        return 'en'  # Bahasa Inggris
    elif choice == '3':
        return 'zh'  # Bahasa China
    else:
        print("Pilihan tidak valid, menggunakan default: Bahasa Inggris")
        return 'en'  # Default ke Bahasa Inggris

# Step 1: Pilih bahasa
language = choose_language()

# Step 2: Rekam audio dari mikrofon
duration = 5  # Durasi rekaman dalam detik
sample_rate = 16000  # Sample rate (misalnya 16kHz)
audio_data = record_audio(duration, sample_rate)

# Step 3: Inference dengan model STT sesuai bahasa yang dipilih
transcription = transcribe_audio_with_language(audio_data, sample_rate, language)
print("Transcription without punctuation:", transcription)

# Step 4: Post-processing (menambahkan tanda baca)
transcription_with_punctuation = add_punctuation(transcription)
print("Transcription with punctuation:", transcription_with_punctuation)

# Step 5: Menyimpan hasil transkripsi ke file teks
output_path = f"data/transcriptions/live_transcription_{language}.txt"
with open(output_path, "w") as f:
    f.write(transcription_with_punctuation)
print(f"Transcription saved to {output_path}")
