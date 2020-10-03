import pyaudio
import wave
from decor import *

class CaptureAudio:
    def __init__(self):
        self.FORMAT=pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.CHUNK = 1024
        self.audio = pyaudio.PyAudio()
        self.frames = []

    @audio_record_thread    
    def startRecording(self):
        stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)            
        while(True):
            data = stream.read(self.CHUNK)
            self.frames.append(data)
            #todo: apply end_record event here
            #along with stream.stop_stream()

    def saveAudioFile(self, filename):
        wavfile = wave.open(filename, 'wb')
        wavfile.setnchannels(self.CHANNELS)
        wavfile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        wavfile.setframerate(self.RATE)
        wavfile.writeframes(b''.join(self.frames))
        wavfile.close()

    def __del__(self):
        self.audio.terminate()

