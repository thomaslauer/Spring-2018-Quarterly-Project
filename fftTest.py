import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack
import sounddevice as sd
import matplotlib.pyplot as plt

fs = 44100  # Set sampling frequency to 44100 hz
duration = 0.1

def main():
    #f = 1  # Frequency, in cycles per second, or Hertz
    #f_s = 100  # Sampling rate, or number of measurements per second

    #t = np.linspace(0, 2, 2 * f_s, endpoint=False)
    #x = np.sin(f * 2 * np.pi * t)

    sample = sd.rec(int(fs*duration), samplerate=fs, channels=1, dtype='int16', blocking=1)
    sample = np.delete(sample,np.s_[0:int(len(sample)*0.05)])

    plotFFT(sample, fs)

def performFFT(sample, fs):

    fft = fftpack.fft(sample)
    freqs = fftpack.fftfreq(len(fft)) * fs

    return freqs, np.abs(fft)

def plotFFT(sample, fs):
    fig, ax = plt.subplots()
    freqs, fft = performFFT(sample, fs)
    ax.stem(freqs, fft)
    ax.set_xlabel('Frequency in Hertz [Hz]')
    ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
    ax.set_xlim(-fs / 2, fs / 2)
    #ax.set_ylim(-5, 110)
    plt.show()

main()