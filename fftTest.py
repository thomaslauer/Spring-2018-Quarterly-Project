import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack


def main():
    f = 10  # Frequency, in cycles per second, or Hertz
    f_s = 100  # Sampling rate, or number of measurements per second

    t = np.linspace(0, 2, 2 * f_s, endpoint=False)
    x = np.sin(f * 2 * np.pi * t)

    plotFFT(x, f_s)

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
    ax.set_ylim(-5, 110)
    plt.show()

main()