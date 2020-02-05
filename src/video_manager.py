from moviepy.editor import *
from constants import CONSTANTS
import cv2
import numpy as np
import glob


class VideoManager:
    """VideoManager handles the process of generating videos. 
    It uses classes audio, media and text."""

    def __init__(self): 
        print("VM")
    # def set_background(self):
    # def make_frame(self, t): 
    # def format_image(self, path):
    #     img_array = []
    #     for filename in glob.glob('../assets/*.png'):
    #         img = cv2.imread(filename)
    #         height, width, layers = img.shape
    #         size = (width,height)
    #         img_array.append(img)