import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack
import sounddevice as sd
import time
import math

# Import Adafruit library and create instance of REST client.
from Adafruit_IO import Client
aio = Client('853a9a70bd2c42508bfcb17a60105477')

fs = 44100  # Set sampling frequency to 44100 hz
duration = 10
sleepTime = 0
threshold = 2000

def main():
    lastTFValue = 0
    while True:
        sample = sd.rec(int(fs*duration), samplerate=fs, channels=1, dtype='int16', blocking=1)
        sample = np.delete(sample,np.s_[0:int(len(sample)*0.05)])

        average = np.average(sample)
        sample = sample - average

        maxVal = np.amax(sample)
        db = 20 * math.log10(maxVal)
        aio.send('decibel-volume', db)

        freqs, fft = performFFT(sample, fs)
        integral = integrateFFT(freqs, fft, 250, 3000)

        aio.send('volume-level', integral) 
        
        if integral > threshold:
            aio.send('on-slash-off', lastTFValue)
            aio.send('on-slash-off', 1)
            lastTFValue = 1
        else:
            aio.send('on-slash-off', lastTFValue)
            aio.send('on-slash-off', 0)
            lastTFValue = 0
            
        print(str(integral))
        time.sleep(sleepTime)


def performFFT(sample, fs):
    fft = fftpack.fft(sample)
    freqs = fftpack.fftfreq(len(fft)) * fs
    return freqs, np.abs(fft)

def plotFFT(sample, fs):
    fig, ax = plt.subplots()
    ax.plot(sample)
    fig, ax = plt.subplots()
    freqs, fft = performFFT(sample, fs)

    fft[0] = 0

    ax.plot(freqs, fft)
    ax.set_xlabel('Frequency in Hertz [Hz]')
    ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')

    ax.set_xlim(0, 2000)

    #ax.set_xlim(-fs / 2, fs / 2)
    #ax.set_ylim(-5, 110)
    print("finished plotting")
    plt.show()

def integrateFFT(freqs, fft, low, high):
    sum = 0
    numSamples = 0
    for i in range(len(freqs)):
        if freqs[i] > low and freqs[i] < high:
            numSamples += 1
            # print("frequency " + str(freqs[i]) + " value " + str(fft[i]))
            sum += fft[i]
    return sum / numSamples


main()
