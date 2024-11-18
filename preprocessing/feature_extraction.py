import librosa
import numpy as np

def extract_mfcc(audio_path, n_mfcc=13):
    y, sr = librosa.load(audio_path)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return mfccs

def extract_mel_spectrogram(audio_path, n_mels=128):
    y, sr = librosa.load(audio_path)
    mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels)
    return mel_spectrogram

def extract_mfcc_batch(audio_paths, n_mfcc=13):
    mfccs_batch = []
    for path in audio_paths:
        mfccs = extract_mfcc(path, n_mfcc)
        mfccs_batch.append(mfccs)
    return mfccs_batch

def extract_mel_spectrogram_batch(audio_paths, n_mels=128):
    mel_spectrogram_batch = []
    for path in audio_paths:
        mel_spectrogram = extract_mel_spectrogram(path, n_mels)
        mel_spectrogram_batch.append(mel_spectrogram)
    return mel_spectrogram_batch