import numpy as np
import scipy.signal

def reduce_noise(audio_data, noise_reduction_level=0.1):
    """Reduce noise in an audio signal using Wiener filter."""
    reduced_noise_audio = scipy.signal.wiener(audio_data, noise_reduction_level)
    return reduced_noise_audio

def spectral_subtraction(audio_data, noise_estimate):
    """Reduce noise using spectral subtraction."""
    audio_fft = np.fft.fft(audio_data)
    noise_fft = np.fft.fft(noise_estimate)
    clean_fft = audio_fft - noise_fft
    clean_audio = np.fft.ifft(clean_fft)
    return np.real(clean_audio)

def median_filter(audio_data, kernel_size=3):
    """Reduce noise using a median filter."""
    return scipy.signal.medfilt(audio_data, kernel_size)

def low_pass_filter(audio_data, cutoff_freq, sample_rate):
    """Reduce high-frequency noise using a low-pass filter."""
    nyquist = 0.5 * sample_rate
    normal_cutoff = cutoff_freq / nyquist
    b, a = scipy.signal.butter(1, normal_cutoff, btype='low', analog=False)
    filtered_audio = scipy.signal.lfilter(b, a, audio_data)
    return filtered_audio