from video_manager import *
import os
import glob
from natsort import natsorted
from moviepy.editor import *
from moviepy.video.fx.resize import resize

def main():
    # videoManager = VideoManager()
    # videoManager.format_image("daium") 
    gif_name = 'pic'
    fps = 24

    file_list = glob.glob('D:\\Work\\BestFIVE\\assets\\*.jpg')  # Get all the pngs in the current directory
    file_list_sorted = natsorted(file_list,reverse=False)  # Sort the images
    clips = []
    for i, item in enumerate(file_list_sorted):
        if i%2==0:
            clip = ImageClip(item).set_pos("left","top")
            clip = resize(clip, width=640,height=480)
        else:   
            clip = ImageClip(item).set_pos("right","bottom")
            clip = resize(clip, width=400,height=300)
        clip = clip.set_duration(1).set_start(i)
        clips.append(clip) 

    concat_clip = CompositeVideoClip(clips,  size = (1280,720))
    concat_clip.write_videofile("test.mp4", fps=fps)

if __name__ == "__main__":
    main()
