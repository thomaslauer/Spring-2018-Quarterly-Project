import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack
import sounddevice as sd
import matplotlib.pyplot as plt

fs = 44100  # Set sampling frequency to 44100 hz
duration = 1.5


def main():

    sample = sd.rec(int(fs*duration), samplerate=fs, channels=1, dtype='int16', blocking=1)
    sample = np.delete(sample,np.s_[0:int(len(sample)*0.05)])
    print("finished recording sound")

    print("Normalizing sample")
    average = np.average(sample)
    
    sample = sample - average
    print("Finished, average is now " + str(np.average(sample)))
    
    plotFFT(sample, fs)

def performFFT(sample, fs):
    print("running fft")
    fft = fftpack.fft(sample) 
    freqs = fftpack.fftfreq(len(fft)) * fs
    print("fft finished")
    return freqs, np.abs(fft)

def plotFFT(sample, fs):
    print("plotting sample")
    fig, ax = plt.subplots()
    ax.plot(sample)
    fig, ax = plt.subplots()
    freqs, fft = performFFT(sample, fs)

    fft[0] = 0

    ax.plot(freqs, fft)
    ax.set_xlabel('Frequency in Hertz [Hz]')
    ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')

    ax.set_xlim(0, 5000)

    #ax.set_xlim(-fs / 2, fs / 2)
    #ax.set_ylim(-5, 110)
    print("finished plotting")
    plt.show()

main()