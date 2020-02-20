from moviepy.editor import *
import cv2
from moviepy.editor import *
from moviepy.video.fx.resize import resize
import numpy as np
from processors.media import *


class VideoManager:
    """VideoManager handles the process of generating videos. 
    It uses classes audio, media and text."""

    def __init__(self):
        print("VideoManager Init")
        self.clip = None
        self.mediaProcessor = MediaProcessor()

    def getVideoFromImages(self, directory_path):
        self.clip = self.mediaProcessor.generateVideoFromDirectoryOfImages(
            directory_path
        )

    def writeFinalVideo(self, output_file_path):
        self.clip.write_videofile(output_file_path, fps=FPS)
