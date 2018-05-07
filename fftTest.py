import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack
import sounddevice as sd
import matplotlib.pyplot as plt

fs = 44100  # Set sampling frequency to 44100 hz
duration = 0.15

def main():

    sample = sd.rec(int(fs*duration), samplerate=fs, channels=1, dtype='int16', blocking=1)
    sample = np.delete(sample,np.s_[0:int(len(sample)*0.50)])

    plotFFT(sample, fs)

def performFFT(sample, fs):

    fft = fftpack.fft(sample)
    freqs = fftpack.fftfreq(len(fft)) * fs

    return freqs, np.abs(fft)

def plotFFT(sample, fs):
    fig, ax = plt.subplots()
    ax.plot(sample)

    fig, ax = plt.subplots()
    freqs, fft = performFFT(sample, fs)
    ax.stem(freqs, fft)
    ax.set_xlabel('Frequency in Hertz [Hz]')
    ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')

    ax.set_xlim(0, 3000)

    #ax.set_xlim(-fs / 2, fs / 2)
    #ax.set_ylim(-5, 110)
    plt.show()

main()