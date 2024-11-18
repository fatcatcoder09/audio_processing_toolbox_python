import numpy as np

def signal_to_noise_ratio(signal, noise):
    signal_power = np.mean(signal**2)
    noise_power = np.mean(noise**2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

def root_mean_square_error(reference, target):
    rmse = np.sqrt(np.mean((reference - target)**2))
    return rmse

def signal_to_noise_ratio_batch(signal_batch, noise_batch):
    snr_batch = []
    for signal, noise in zip(signal_batch, noise_batch):
        snr = signal_to_noise_ratio(signal, noise)
        snr_batch.append(snr)
    return snr_batch

def root_mean_square_error_batch(reference_batch, target_batch):
    rmse_batch = []
    for reference, target in zip(reference_batch, target_batch):
        rmse = root_mean_square_error(reference, target)
        rmse_batch.append(rmse)
    return rmse_batch