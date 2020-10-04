import cv2
import pyautogui
import pyaudio
import numpy as np
from threading import Thread
from screencapture import *
from audiocapture import *

class ScreenRecorder:
    def __init__(self):
        self.audio = CaptureAudio()
        self.video = ScreenCapture()

    def startRecoding(self):
        t1 = Thread(target=self.audio.startRecording)
        t2 = Thread(target=self.video.recordScreen, args=("tempfile.avi"))
        t1.start()
        t2.start()