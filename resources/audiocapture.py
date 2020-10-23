
import pyaudio
import wave
import cv2
# from decor import *


class CaptureAudio:
    def __init__(self):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.CHUNK = 1024
        # if it is False then the recoding should stop .Intially it is true indicating that the recording should start
        self.isRecord = True
        self.audio = pyaudio.PyAudio()  # opens an audio channel
        self.frames = []

    def startRecoding(self, filename):
        # initialises audio stream and starts recording
        stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                                 rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        print("Started Recording Audio")
        while True:
            data = stream.read(self.CHUNK)
            self.frames.append(data)
            if not self.isRecord:
                break

        stream.stop_stream()
        stream.close()
        self.saveAudioFile(filename)
        # todo: apply end_record event here
        # along with stream.stop_stream()

    def saveAudioFile(self, filename):
        print("Saving Recorded Audio")
        wavfile = wave.open(filename, 'wb')
        wavfile.setnchannels(self.CHANNELS)
        wavfile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        wavfile.setframerate(self.RATE)
        wavfile.writeframes(b''.join(self.frames))
        wavfile.close()

    def __del__(self):
        self.audio.terminate()  # terminates the pyaudio object
