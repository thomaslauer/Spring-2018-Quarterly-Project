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
duration = 1
sleepTime = 0
threshold = 250
ARRAY_SIZE = 4

def main():

    averageArray = np.zeros(ARRAY_SIZE)

    lastTFValue = -1
    while True:
        sample = sd.rec(int(fs*duration), samplerate=fs, channels=1, dtype='int16', blocking=1)
        sample = np.delete(sample,np.s_[0:int(len(sample)*0.05)])

        average = np.average(sample)
        sample = sample - average

        maxVal = np.amax(sample)
        db = 20 * math.log10(maxVal)
        aio.send('decibel-volume', db)

        freqs, fft = performFFT(sample, fs)
        integral = integrateFFT(freqs, fft, 250, 3000)/duration

        print("Array is " + str(averageArray))
        np.roll(averageArray, 1)
        if integral > threshold:
            averageArray[0] = 1
        else:
            averageArray[0] = 0

        print("Average is " + str(np.average(averageArray)))
        print("Array is " + str(averageArray))


        aio.send('volume-level', integral) 
        
        if integral > threshold:
            if lastTFValue != -1:
                aio.send('on-slash-off', lastTFValue)
            
            aio.send('on-slash-off', 1)
            lastTFValue = 1
        else:   
            if lastTFValue != -1:
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

    print("finished plotting")
    plt.show()

def integrateFFT(freqs, fft, low, high):
    sum = 0
    numSamples = 0
    for i in range(len(freqs)):
        if freqs[i] > low and freqs[i] < high:
            numSamples += 1
            sum += fft[i]
    return sum / numSamples


main()
