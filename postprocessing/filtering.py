from scipy.signal import butter, lfilter

def butter_lowpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_highpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def lowpass_filter_batch(data_batch, cutoff, fs, order=5):
    filtered_batch = []
    for data in data_batch:
        filtered_data = lowpass_filter(data, cutoff, fs, order)
        filtered_batch.append(filtered_data)
    return filtered_batch

def highpass_filter_batch(data_batch, cutoff, fs, order=5):
    filtered_batch = []
    for data in data_batch:
        filtered_data = highpass_filter(data, cutoff, fs, order)
        filtered_batch.append(filtered_data)
    return filtered_batch