import numpy as np

def align_signals(reference, target):
    correlation = np.correlate(reference, target, mode='full')
    delay = np.argmax(correlation) - len(target) + 1
    aligned_target = np.roll(target, delay)
    return aligned_target

def align_signals_batch(reference_batch, target_batch):
    aligned_batch = []
    for reference, target in zip(reference_batch, target_batch):
        aligned_target = align_signals(reference, target)
        aligned_batch.append(aligned_target)
    return aligned_batch