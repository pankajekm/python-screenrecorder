import numpy
import cv2
from threading import Thread
from screencapture import *
from audiocapture import *
import tkinter as tk
from tkinter.font import Font


class ScreenRecorder(object):
    def __init__(self):
        self.audio = CaptureAudio()
        self.video = ScreenCapture()

    def startRecoding(self):
        T1 = Thread(target=self.video.recordScreen,
                    args=("video.avi",))
        T2 = Thread(target=self.audio.startRecoding, args=("audio.wav",))
        T1.start()
        T2.start()

    def stopRecording(self):
        self.audio.isRecord = False
        self.video.isRecord = False

    def pause(self):
        print("Not implemented yet")


def main():
    recorder = ScreenRecorder()

    # GUI
    root = tk.Tk()
    root.geometry('300x80')
    root.title("Recorder")
    root.configure(background='black')

    btnStart = tk.Button(root, text='Start', bd='3', background='white',
                         command=recorder.startRecoding)
    btnStop = tk.Button(root, text='Pause/Resume', bd='3', background='green', command=recorder.pause
                        )
    btnPause = tk.Button(root, text='Stop', bd='3', background='red', command=recorder.stopRecording
                         )

    btnStart.place(x=3, y=4)
    btnStop.place(x=100, y=4)
    btnPause.place(x=250, y=4)
    root.mainloop()


main()
