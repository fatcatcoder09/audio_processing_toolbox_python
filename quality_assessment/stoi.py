
import numpy as np
from scipy.io import wavfile
from pystoi import stoi

def calculate_stoi(reference_file, degraded_file, sample_rate=16000):
    """
    Calculate STOI (Short-Time Objective Intelligibility) score between a reference and a degraded audio file.
    
    Args:
        reference_file (str): Path to the reference audio file.
        degraded_file (str): Path to the degraded audio file.
        sample_rate (int): Sample rate of the audio files (default is 16000).
        
    Returns:
        float: STOI score.
    """
    try:
        sr_ref, ref = wavfile.read(reference_file)
        sr_deg, deg = wavfile.read(degraded_file)
        
        if sr_ref != sample_rate or sr_deg != sample_rate:
            raise ValueError("Sample rate of the audio files must match the specified sample rate.")
        
        ref = ref.astype(np.float32)
        deg = deg.astype(np.float32)
        
        return stoi(ref, deg, sample_rate)
    except Exception as e:
        print(f"Error calculating STOI: {e}")
        return None