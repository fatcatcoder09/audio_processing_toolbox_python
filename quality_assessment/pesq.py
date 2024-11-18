import subprocess

def calculate_pesq(reference_file, degraded_file, sample_rate=16000):
    """
    Calculate PESQ (Perceptual Evaluation of Speech Quality) score between a reference and a degraded audio file.
    
    Args:
        reference_file (str): Path to the reference audio file.
        degraded_file (str): Path to the degraded audio file.
        sample_rate (int): Sample rate of the audio files (default is 16000).
        
    Returns:
        float: PESQ score.
    """
    try:
        result = subprocess.run(
            ['pesq', f'+{sample_rate}', reference_file, degraded_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output = result.stdout
        pesq_score = float(output.split()[-1])
        return pesq_score
    except Exception as e:
        print(f"Error calculating PESQ: {e}")
        return None
