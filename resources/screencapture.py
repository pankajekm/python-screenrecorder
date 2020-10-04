import cv2
import numpy as np
import os
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
    self.FOURCC = cv2.VideoWriter_fourcc(*'mp4v')
    img = pyautogui.screenshot()
    self.height, self.width, self.channels = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR).shape

  def recordScreen(self, filename):
    with WriteVideoToFile(filename, self.FOURCC, 20.0, (self.width, self.height)) as out:
      while(True):
        try:
          image = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)
          out.write(image)
          StopIteration(0.5)
        except KeyboardInterrupt:
          pass
