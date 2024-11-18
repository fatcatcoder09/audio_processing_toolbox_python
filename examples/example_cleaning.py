
from audio_processing_toolbox.cleaning import remove_noise, remove_silence, detect_outliers
from audio_processing_toolbox.io import load_audio, save_audio

# Load audio data
audio_data = load_audio('path/to/audio/file.wav')

# Remove noise
cleaned_audio = remove_noise(audio_data)

# Remove silence
cleaned_audio = remove_silence(cleaned_audio)

# Detect outliers
outliers = detect_outliers(cleaned_audio)

# Save cleaned audio
save_audio(cleaned_audio, 'path/to/cleaned_audio/file.wav')