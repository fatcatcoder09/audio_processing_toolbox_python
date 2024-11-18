# Import PESQ assessment tool
from .pesq import calculate_pesq

# Import other quality assessment algorithms
from .stoi import calculate_stoi
from .ssnr import calculate_ssnr
from .snr import calculate_snr
from .llr import calculate_llr
from .fwseg_snr import calculate_fwseg_snr

# Mapping of method names to functions
quality_assessment_methods = {
    'pesq': calculate_pesq,
    'stoi': calculate_stoi,
    'ssnr': calculate_ssnr,
    'snr': calculate_snr,
    'llr': calculate_llr,
    'fwseg_snr': calculate_fwseg_snr
}

# Interface function for quality assessment module
def assess_quality(signal, reference, method='pesq'):
    if method in quality_assessment_methods:
        return quality_assessment_methods[method](signal, reference)
    else:
        raise ValueError(f"Unknown quality assessment method: {method}")
