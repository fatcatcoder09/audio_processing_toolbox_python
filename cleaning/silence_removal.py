from pydub import AudioSegment
from pydub.silence import split_on_silence, detect_nonsilent

def remove_silence(audio_segment, silence_thresh=-40, min_silence_len=500):
    """Remove silence from an audio segment."""
    chunks = split_on_silence(audio_segment, silence_thresh=silence_thresh, min_silence_len=min_silence_len)
    non_silent_audio = AudioSegment.empty()
    for chunk in chunks:
        non_silent_audio += chunk
    return non_silent_audio

def trim_silence(audio_segment, silence_thresh=-40):
    """Trim leading and trailing silence from an audio segment."""
    nonsilent_ranges = detect_nonsilent(audio_segment, min_silence_len=100, silence_thresh=silence_thresh)
    if nonsilent_ranges:
        start_trim = nonsilent_ranges[0][0]
        end_trim = nonsilent_ranges[-1][1]
        trimmed_audio = audio_segment[start_trim:end_trim]
        return trimmed_audio
    return audio_segment

def detect_silence(audio_segment, silence_thresh=-40, min_silence_len=500):
    """Detect silence segments in an audio segment."""
    silence_ranges = detect_nonsilent(audio_segment, min_silence_len=min_silence_len, silence_thresh=silence_thresh)
    return silence_ranges