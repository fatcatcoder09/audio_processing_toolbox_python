import librosa
import soundfile as sf
from pydub import AudioSegment
import os

def load_audio(file_path, sr=22050):
    audio, sample_rate = librosa.load(file_path, sr=sr)
    return audio, sample_rate

def save_audio(file_path, audio, sr):
    sf.write(file_path, audio, sr)

def load_audio_pydub(file_path):
    """Load an audio file using pydub."""
    audio = AudioSegment.from_file(file_path)
    return audio

def save_audio_pydub(file_path, audio, format):
    """Save an audio file using pydub."""
    audio.export(file_path, format=format)

def get_audio_metadata(file_path):
    """Get metadata of an audio file."""
    audio = AudioSegment.from_file(file_path)
    return {
        "duration": len(audio) / 1000.0,  # duration in seconds
        "channels": audio.channels,
        "frame_rate": audio.frame_rate,
        "sample_width": audio.sample_width
    }

def load_audio_batch(directory, sr=22050):
    audio_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.wav')]
    audio_data = []
    for file in audio_files:
        audio, sample_rate = load_audio(file, sr)
        audio_data.append((audio, sample_rate))
    return audio_data

def save_audio_batch(directory, audio_data):
    for i, (audio, sr) in enumerate(audio_data):
        file_path = os.path.join(directory, f'audio_{i}.wav')
        save_audio(file_path, audio, sr)
