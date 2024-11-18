
import numpy as np
from scipy.io import wavfile

def calculate_ssnr(reference_file, degraded_file):
    """
    Calculate SSNR (Segmental Signal-to-Noise Ratio) between a reference and a degraded audio file.
    
    Args:
        reference_file (str): Path to the reference audio file.
        degraded_file (str): Path to the degraded audio file.
        
    Returns:
        float: SSNR value in dB.
    """
    try:
        sr_ref, ref = wavfile.read(reference_file)
        sr_deg, deg = wavfile.read(degraded_file)
        
        if sr_ref != sr_deg:
            raise ValueError("Sample rates of the audio files must match.")
        
        frame_size = int(sr_ref * 0.03)  # 30ms frames
        ssnr = 0
        num_frames = 0
        
        for i in range(0, len(ref) - frame_size, frame_size):
            ref_frame = ref[i:i + frame_size]
            deg_frame = deg[i:i + frame_size]
            noise_frame = ref_frame - deg_frame
            ssnr += 10 * np.log10(np.mean(ref_frame**2) / np.mean(noise_frame**2))
            num_frames += 1
        
        return ssnr / num_frames
    except Exception as e:
        print(f"Error calculating SSNR: {e}")
        return None