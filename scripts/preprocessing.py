import librosa
import soundfile as sf

def load_audio(file_path, target_sr=16000):
    """
    Memuat file audio, melakukan resampling jika perlu, dan mengembalikan data audio dan sample rate.
    
    Args:
        file_path (str): Path file audio input.
        target_sr (int): Sample rate yang diinginkan (default 16kHz).
        
    Returns:
        audio (numpy.ndarray): Data audio yang sudah di-resample.
        sample_rate (int): Sample rate setelah pemuatan.
    """
    # Load audio dan resampling sesuai dengan target_sr
    audio, sr = librosa.load(file_path, sr=target_sr)
    return audio, sr

def save_audio(audio, sample_rate, output_path):
    """
    Menyimpan data audio dalam format .wav.
    
    Args:
        audio (numpy.ndarray): Data audio yang akan disimpan.
        sample_rate (int): Sample rate audio.
        output_path (str): Path untuk menyimpan file output audio.
    """
    sf.write(output_path, audio, sample_rate)
