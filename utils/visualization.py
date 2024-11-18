import matplotlib.pyplot as plt
import librosa.display

def plot_waveform(audio, sr):
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(audio, sr=sr)
    plt.title('Waveform')
    plt.show()

def plot_spectrogram(spectrogram, sr, hop_length):
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(librosa.amplitude_to_db(spectrogram, ref=np.max), sr=sr, hop_length=hop_length, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')
    plt.show()

def plot_waveform_batch(audio_batch, sr):
    for audio in audio_batch:
        plot_waveform(audio, sr)

def plot_spectrogram_batch(spectrogram_batch, sr, hop_length):
    for spectrogram in spectrogram_batch:
        plot_spectrogram(spectrogram, sr, hop_length)