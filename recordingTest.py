import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

fs = 44100  # Set sampling frequency to 44100 hz
duration = 3


def main():

    sample = sd.rec(int(fs*duration), samplerate=fs, channels=1, dtype='int16', blocking=1)

    sample = np.delete(sample,np.s_[0:int(len(sample)*0.05)])


    sd.play(sample, fs)
    
    print(len(sample))
    plt.figure(1)
    plt.title('Signal Wave...')
    plt.plot(sample)
    plt.show()

main()