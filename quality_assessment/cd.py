
import numpy as np
from scipy.io import wavfile
from python_speech_features import mfcc

def calculate_cd(reference_file, degraded_file):
    """
    Calculate CD (Cepstral Distance) between a reference and a degraded audio file.
    
    Args:
        reference_file (str): Path to the reference audio file.
        degraded_file (str): Path to the degraded audio file.
        
    Returns:
        float: CD value.
    """
    try:
        sr_ref, ref = wavfile.read(reference_file)
        sr_deg, deg = wavfile.read(degraded_file)
        
        if sr_ref != sr_deg:
            raise ValueError("Sample rates of the audio files must match.")
        
        ref_mfcc = mfcc(ref, sr_ref)
        deg_mfcc = mfcc(deg, sr_deg)
        
        cd = np.mean(np.sqrt(np.sum((ref_mfcc - deg_mfcc)**2, axis=1)))
        
        return cd
    except Exception as e:
        print(f"Error calculating CD: {e}")
        return None