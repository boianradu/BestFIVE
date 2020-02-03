from moviepy.editor import *
import gizeh
import numpy as np
from constants import CONSTANTS

class VideoManager:
    """VideoManager handles the process of generating videos. 
    It uses classes audio, media and text."""

    def __init__(self):
        super(VideoManager, self).__init__()
        self.TAG = "Video Manager"
        self.movieClip = VideoClip(make_frame=self.make_frame, duration=3)
        # self.movieClip.size=(1280,720)
        self.CONSTANTS=CONSTANTS.getInstance()
        print("Current class:", self.TAG)

    # def set_background(self):
    def make_frame(self, t):
        surface = gizeh.Surface(1280,720) # width, height
        # radius = W*(1+ (t*(2-t))**2 )/6 # the radius varies over time
        # circle = gizeh.circle(radius, xy = (64,64), fill=(1,0,0))
        # circle.draw(surface)
        return surface.get_npimage() # returns a 8-bit RGB array

    def format_image(self, path):
        self.movieClip.set_duration(3).write_videofile("movie.mp4", 30) 