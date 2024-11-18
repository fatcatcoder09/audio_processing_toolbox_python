from pydub import AudioSegment

def convert_format(input_file, output_file, output_format):
    """Convert audio file format."""
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format=output_format)

def change_sample_rate(input_file, output_file, new_sample_rate):
    """Change the sample rate of an audio file."""
    audio = AudioSegment.from_file(input_file)
    audio = audio.set_frame_rate(new_sample_rate)
    audio.export(output_file, format="wav")

def adjust_volume(input_file, output_file, volume_change_dB):
    """Adjust the volume of an audio file."""
    audio = AudioSegment.from_file(input_file)
    audio = audio + volume_change_dB
    audio.export(output_file, format="wav")
