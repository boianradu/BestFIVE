from natsort import natsorted
from configs.constants import *
from moviepy.editor import *
from moviepy.video.fx.resize import resize
import glob

class MediaProcessor:
    """MediaProcessor handles images, gifs and videos to merge them
    into a final video."""

    def __init__(self):
        super(MediaProcessor, self).__init__()
        self.TAG = "Media Processor"
        self.clips=[]
        print("Current class:", self.TAG)

    def generateImage(self, image_path, duration, start_time):
        '''
            generate image clip style
        ''' 
        imageClip = ImageClip(image_path).set_pos("center","center")
        imageClip=resize(imageClip,width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
        imageClip=imageClip.set_duration(duration).set_start(start_time)
        return imageClip

    def generateVideoFromDirectoryOfImages(self, directory_path):
        '''
            generate video from directory of images specified
        '''
        file_list = glob.glob(directory_path)
        file_list_sorted = natsorted(file_list, reverse=False)
        for i, item in enumerate(file_list_sorted):
            self.clips.append(self.generateImage(item,TIME_IMAGE_SMALL, i))
        final_clip = CompositeVideoClip(self.clips, size = (SCREEN_HEIGHT, SCREEN_WIDTH))
        return final_clip