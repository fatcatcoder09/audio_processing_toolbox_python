import numpy as np

def detect_outliers(audio_data, threshold=3.0):
    """Detect outliers in an audio signal."""
    mean = np.mean(audio_data)
    std_dev = np.std(audio_data)
    outliers = np.where(np.abs(audio_data - mean) > threshold * std_dev)
    return outliers

def remove_outliers(audio_data, threshold=3.0):
    """Remove outliers from an audio signal."""
    outliers = detect_outliers(audio_data, threshold)
    cleaned_audio = np.copy(audio_data)
    cleaned_audio[outliers] = np.median(audio_data)
    return cleaned_audio

def replace_outliers(audio_data, threshold=3.0, replacement_value=0):
    """Replace outliers in an audio signal with a specified value."""
    outliers = detect_outliers(audio_data, threshold)
    cleaned_audio = np.copy(audio_data)
    cleaned_audio[outliers] = replacement_value
    return cleaned_audio