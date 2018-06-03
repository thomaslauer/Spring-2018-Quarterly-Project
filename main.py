import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack
import sounddevice as sd
import time
import math

"""
This is the main program for the washing machine monitor
"""

# Import Adafruit library and create instance of REST client.
from Adafruit_IO import Client
aio = Client('853a9a70bd2c42508bfcb17a60105477')

fs = 44100  # Set sampling frequency to 44100 hz
duration = 10
sleepTime = 0
threshold = 250
ARRAY_SIZE = 6

# if more then 1/3 of the signals were positive, we're going to count it as
# active
ARRAY_THRESHOLD = .33

def main():

    a = [0] * ARRAY_SIZE
    numIterations = 0

    lastTFValue = -1
    while True:
        numIterations += 1

        # Record a sound
        sample = sd.rec(int(fs*duration), samplerate=fs, channels=1, dtype='int16', blocking=1)
        
        # Remove the first 5% of the sound (This helped on some computers)
        sample = np.delete(sample,np.s_[0:int(len(sample)*0.05)])

        # normalize the sample around an average of 0
        average = np.average(sample)
        sample = sample - average
        
        # Perform the FFT
        freqs, fft = performFFT(sample, fs)

        # Calculate the average value, and normalize it for the sound duration
        integral = integrateFFT(freqs, fft, 250, 3000)/duration

        # if it's above the threshold, set the ON value in the array
        if integral > threshold:
            a = [1] + a[:ARRAY_SIZE-1]
        else:
            a = [0] + a[:ARRAY_SIZE-1]

        aio.send('volume-level', integral) 
        
        if numIterations > ARRAY_SIZE:
            # If we haven't had enough samples, don't report any on/off data
            if sum(a)/ARRAY_SIZE > ARRAY_THRESHOLD:
                # It's currently active!
                if lastTFValue != -1:
                    aio.send('on-slash-off', lastTFValue)
                
                aio.send('on-slash-off', 1)
                aio.send('status-text', 'Wash On')
                lastTFValue = 1
            else:   
                # It's inactive right now
                if lastTFValue != -1:
                    aio.send('on-slash-off', lastTFValue)
                
                aio.send('on-slash-off', 0)
                aio.send('status-text', 'Wash Off')
                lastTFValue = 0
        
        print(str(integral))
        time.sleep(sleepTime)


def performFFT(sample, fs):
    """
    This function performs an fft on the sample, given a sampling rate fs

    It returns a list of frequencies, and a list of the amplitudes
    """
    fft = fftpack.fft(sample)
    freqs = fftpack.fftfreq(len(fft)) * fs
    return freqs, np.abs(fft)

def plotFFT(sample, fs):
    """"
    Plot an fft from a sample
    """
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
    """
    This samples an fft and averages all the frequencies between low and high
    """
    sum = 0
    numSamples = 0
    for i in range(len(freqs)):
        if freqs[i] > low and freqs[i] < high:
            numSamples += 1
            sum += fft[i]
    return sum / numSamples


main()
