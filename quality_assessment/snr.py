
import numpy as np
from scipy.io import wavfile

def calculate_snr(reference_file, degraded_file):
    """
    Calculate SNR (Signal-to-Noise Ratio) between a reference and a degraded audio file.
    
    Args:
        reference_file (str): Path to the reference audio file.
        degraded_file (str): Path to the degraded audio file.
        
    Returns:
        float: SNR value in dB.
    """
    try:
        sr_ref, ref = wavfile.read(reference_file)
        sr_deg, deg = wavfile.read(degraded_file)
        
        if sr_ref != sr_deg:
            raise ValueError("Sample rates of the audio files must match.")
        
        noise = ref - deg
        snr = 10 * np.log10(np.mean(ref**2) / np.mean(noise**2))
        
        return snr
    except Exception as e:
        print(f"Error calculating SNR: {e}")
        return None