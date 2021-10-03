##  This code is used to record the command user gives to play the songs. The recorded audio is saved as waveform by using this code.

import sounddevice as sd
import OpenSSL.tsafe
from scipy.io.wavfile import write

def record():
    fs = 44100  # Sample rate
    seconds = 5  # Duration of recording
    
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('myfile.wav', fs, myrecording)  # Save as WAV file
