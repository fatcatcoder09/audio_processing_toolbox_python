from audio_processing_toolbox.io.loaders import load_audio
from audio_processing_toolbox.cleaning.noise_reduction import reduce_noise
from audio_processing_toolbox.cleaning.silence_removal import remove_silence
from audio_processing_toolbox.preprocessing.feature_extraction import extract_mfcc
from audio_processing_toolbox.preprocessing.normalization import normalize_audio
from audio_processing_toolbox.postprocessing.enhancement import enhance_audio
from audio_processing_toolbox.postprocessing.alignment import align_audio
from audio_processing_toolbox.utils.visualization import plot_waveform
from audio_processing_toolbox.utils.metrics import calculate_snr

def main():
    # Load audio file
    audio_data, sample_rate = load_audio('path/to/audio/file.wav')
    print("Audio loaded.")

    # Reduce noise
    cleaned_audio = reduce_noise(audio_data, sample_rate)
    print("Noise reduced.")

    # Remove silence
    audio_no_silence = remove_silence(cleaned_audio, sample_rate)
    print("Silence removed.")

    # Normalize audio
    normalized_audio = normalize_audio(audio_no_silence)
    print("Audio normalized.")

    # Extract MFCC features
    mfcc_features = extract_mfcc(normalized_audio, sample_rate)
    print("MFCC features extracted.")

    # Enhance audio
    enhanced_audio = enhance_audio(normalized_audio, sample_rate)
    print("Audio enhanced.")

    # Align audio
    aligned_audio = align_audio(enhanced_audio, sample_rate)
    print("Audio aligned.")

    # Calculate SNR
    snr = calculate_snr(audio_data, aligned_audio)
    print(f"Signal-to-Noise Ratio (SNR): {snr} dB")

    # Plot waveform
    plot_waveform(aligned_audio, sample_rate)
    print("Waveform plotted.")

if __name__ == "__main__":
    main()