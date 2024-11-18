import numpy as np

def segment_audio(audio, segment_length):
    segments = []
    for start in range(0, len(audio), segment_length):
        end = start + segment_length
        segments.append(audio[start:end])
    return segments

def segment_audio_batch(audio_batch, segment_length):
    segmented_batch = []
    for audio in audio_batch:
        segments = segment_audio(audio, segment_length)
        segmented_batch.append(segments)
    return segmented_batch