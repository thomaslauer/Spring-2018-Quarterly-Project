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
duration = 5
sleepTime = 0
threshold = 250
ARRAY_SIZE = 4
ARRAY_THRESHOLD = 0.5

def main():

    a = [0] * ARRAY_SIZE
    numIterations = 0

    lastTFValue = -1
    while True:
        numIterations += 1
        sample = sd.rec(int(fs*duration), samplerate=fs, channels=1, dtype='int16', blocking=1)
        sample = np.delete(sample,np.s_[0:int(len(sample)*0.05)])

        average = np.average(sample)
        sample = sample - average

        freqs, fft = performFFT(sample, fs)
        integral = integrateFFT(freqs, fft, 250, 3000)/duration



        if integral > threshold:
            a = [1] + a[:ARRAY_SIZE-1]
        else:
            a = [0] + a[:ARRAY_SIZE-1]

        aio.send('volume-level', integral) 
        
        if numIterations > ARRAY_SIZE:
            if sum(a)/ARRAY_SIZE > ARRAY_THRESHOLD:
                if lastTFValue != -1:
                    aio.send('on-slash-off', lastTFValue)
                
                aio.send('on-slash-off', 1)
                aio.send('status-text', 'Wash On')
                lastTFValue = 1
            else:   
                if lastTFValue != -1:
                    aio.send('on-slash-off', lastTFValue)
                
                aio.send('on-slash-off', 0)
                aio.send('status-text', 'Wash Off')
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
