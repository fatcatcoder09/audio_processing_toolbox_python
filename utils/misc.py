import numpy as np

def calculate_rms(audio):
    rms = np.sqrt(np.mean(audio**2))
    return rms

def calculate_zero_crossing_rate(audio):
    zero_crossings = np.sum(np.abs(np.diff(np.sign(audio)))) / len(audio)
    return zero_crossings

def calculate_rms_batch(audio_batch):
    rms_batch = []
    for audio in audio_batch:
        rms = calculate_rms(audio)
        rms_batch.append(rms)
    return rms_batch

def calculate_zero_crossing_rate_batch(audio_batch):
    zcr_batch = []
    for audio in audio_batch:
        zcr = calculate_zero_crossing_rate(audio)
        zcr_batch.append(zcr)
    return zcr_batch