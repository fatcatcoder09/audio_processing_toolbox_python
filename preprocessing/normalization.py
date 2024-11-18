import numpy as np

def normalize_audio(audio, target_level=-20.0):
    rms = np.sqrt(np.mean(audio**2))
    scalar = 10**(target_level / 20) / (rms + 1e-6)
    normalized_audio = audio * scalar
    return normalized_audio

def normalize_audio_batch(audio_batch, target_level=-20.0):
    normalized_batch = []
    for audio in audio_batch:
        normalized_audio = normalize_audio(audio, target_level)
        normalized_batch.append(normalized_audio)
    return normalized_batch