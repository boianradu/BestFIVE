from video_manager import *
import os 
from moviepy.editor import *
from moviepy.video.fx.resize import resize


def main():
    directory_path = "D:\\Work\\BestFIVE\\assets\\*jpg"
    videoManager = VideoManager()
    videoManager.getVideoFromImages(directory_path)
    videoManager.writeFinalVideo("out.mp4")


if __name__ == "__main__":
    main()
