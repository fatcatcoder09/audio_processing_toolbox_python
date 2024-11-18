import numpy as np

def spectral_subtraction(noisy_signal, noise_estimate):
    enhanced_signal = noisy_signal - noise_estimate
    enhanced_signal[enhanced_signal < 0] = 0
    return enhanced_signal

def spectral_subtraction_batch(noisy_signals, noise_estimates):
    enhanced_batch = []
    for noisy_signal, noise_estimate in zip(noisy_signals, noise_estimates):
        enhanced_signal = spectral_subtraction(noisy_signal, noise_estimate)
        enhanced_batch.append(enhanced_signal)
    return enhanced_batch