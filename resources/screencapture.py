import cv2
import numpy as np
import pyautogui


class WriteVideoToFile(cv2.VideoWriter):
    # def __init__(self, filename, fourcc, fps, framesize):
    #   calls the super class __init__ function
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.release()


class ScreenCapture:
    def __init__(self):
        # if it is False then the recoding should stop .Intially it is true indicating that the recording should start
        self.isRecord = True
        self.FOURCC = cv2.VideoWriter_fourcc(*'mp4v')
        img = pyautogui.screenshot()
        self.height, self.width, self.channels = cv2.cvtColor(
            np.array(img), cv2.COLOR_RGB2BGR).shape

    def recordScreen(self, filename):
        print("Recording Video")
        with WriteVideoToFile(filename, self.FOURCC, 8.0, (self.width, self.height)) as out:
            while(True):
                image = cv2.cvtColor(
                    np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
                out.write(image)
                StopIteration(1)
                if not self.isRecord:
                    break
            print("stopped Recording")
