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

    def generate_video(self, directory_path):
        self.mediaProcessor.generate_video_images_directory(directory_path)
        self.mediaProcessor.add_audio_to_video("D:\\Work\\BestFIVE\\assets\\deli.mp3")

    def write_final_video(self, output_file_path):
        self.mediaProcessor.write_final_clip(output_file_path, FPS)
