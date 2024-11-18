
import numpy as np
from scipy.io import wavfile
from scipy.linalg import toeplitz, inv

def calculate_llr(reference_file, degraded_file):
    """
    Calculate LLR (Log-Likelihood Ratio) between a reference and a degraded audio file.
    
    Args:
        reference_file (str): Path to the reference audio file.
        degraded_file (str): Path to the degraded audio file.
        
    Returns:
        float: LLR value.
    """
    try:
        sr_ref, ref = wavfile.read(reference_file)
        sr_deg, deg = wavfile.read(degraded_file)
        
        if sr_ref != sr_deg:
            raise ValueError("Sample rates of the audio files must match.")
        
        frame_size = int(sr_ref * 0.03)  # 30ms frames
        llr = 0
        num_frames = 0
        
        for i in range(0, len(ref) - frame_size, frame_size):
            ref_frame = ref[i:i + frame_size]
            deg_frame = deg[i:i + frame_size]
            
            ref_corr = np.correlate(ref_frame, ref_frame, mode='full')
            deg_corr = np.correlate(deg_frame, deg_frame, mode='full')
            
            ref_corr_matrix = toeplitz(ref_corr[len(ref_corr)//2:])
            deg_corr_matrix = toeplitz(deg_corr[len(deg_corr)//2:])
            
            ref_inv = inv(ref_corr_matrix)
            deg_inv = inv(deg_corr_matrix)
            
            llr += np.log(np.linalg.det(ref_inv @ deg_corr_matrix))
            num_frames += 1
        
        return llr / num_frames
    except Exception as e:
        print(f"Error calculating LLR: {e}")
        return None