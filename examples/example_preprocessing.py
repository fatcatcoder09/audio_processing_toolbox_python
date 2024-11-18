
from audio_processing_toolbox.preprocessing import extract_features, normalize_audio, segment_audio
from audio_processing_toolbox.io import load_audio, save_audio

# Load audio data
audio_data = load_audio('path/to/audio/file.wav')

# Normalize audio
normalized_audio = normalize_audio(audio_data)

# Extract features
features = extract_features(normalized_audio)

# Segment audio
segments = segment_audio(normalized_audio)

# Save normalized audio
save_audio(normalized_audio, 'path/to/normalized_audio/file.wav')