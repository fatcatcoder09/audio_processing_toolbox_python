
from audio_processing_toolbox.postprocessing import apply_filter, enhance_audio, align_audio
from audio_processing_toolbox.io import load_audio, save_audio

# Load audio data
audio_data = load_audio('path/to/audio/file.wav')

# Apply filter
filtered_audio = apply_filter(audio_data)

# Enhance audio
enhanced_audio = enhance_audio(filtered_audio)

# Align audio
aligned_audio = align_audio(enhanced_audio)

# Save enhanced audio
save_audio(enhanced_audio, 'path/to/enhanced_audio/file.wav')