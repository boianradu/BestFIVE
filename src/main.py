from video_manager import *
import os
from moviepy.editor import *
from moviepy.video.fx.resize import resize


def main():
    directory_path = "*jpg"
    videoManager = VideoManager()
    videoManager.generate_video(directory_path)
    videoManager.write_final_video("out.mp4")


if __name__ == "__main__":
    main()

