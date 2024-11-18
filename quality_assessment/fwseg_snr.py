
import numpy as np
from scipy.io import wavfile

def calculate_fwseg_snr(reference_file, degraded_file):
    """
    Calculate FWSEG SNR (Frequency-Weighted Segmental Signal-to-Noise Ratio) between a reference and a degraded audio file.
    
    Args:
        reference_file (str): Path to the reference audio file.
        degraded_file (str): Path to the degraded audio file.
        
    Returns:
        float: FWSEG SNR value in dB.
    """
    try:
        sr_ref, ref = wavfile.read(reference_file)
        sr_deg, deg = wavfile.read(degraded_file)
        
        if sr_ref != sr_deg:
            raise ValueError("Sample rates of the audio files must match.")
        
        frame_size = int(sr_ref * 0.03)  # 30ms frames
        fwseg_snr = 0
        num_frames = 0
        
        for i in range(0, len(ref) - frame_size, frame_size):
            ref_frame = ref[i:i + frame_size]
            deg_frame = deg[i:i + frame_size]
            noise_frame = ref_frame - deg_frame
            
            ref_power = np.sum(ref_frame**2)
            noise_power = np.sum(noise_frame**2)
            
            if noise_power > 0:
                fwseg_snr += 10 * np.log10(ref_power / noise_power)
                num_frames += 1
        
        return fwseg_snr / num_frames
    except Exception as e:
        print(f"Error calculating FWSEG SNR: {e}")
        return None