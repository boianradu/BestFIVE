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
        self.clips = []
        self.clip = VideoClip()
        print("Current class:", self.TAG)

    def generate_image(
        self,
        image_path,
        duration,
        start_time,
        image_width=SCREEN_WIDTH,
        image_height=SCREEN_HEIGHT,
        horizontal_pos="center",
        vertical_pos="center",
    ):
        """
            generate image clip style
        """
        imageClip = ImageClip(image_path).set_position(
            horizontal_pos, vertical_pos
        )  # horizontal-vertical
        imageClip = resize(imageClip, width=image_width, height=image_height)
        imageClip = imageClip.set_duration(duration).set_start(start_time)
        return imageClip

    def generate_video_images_directory(self, directory_path):
        """
            generate video from directory of images specified
        """
        file_list = glob.glob(directory_path)
        file_list_sorted = natsorted(file_list, reverse=False)
        for i, item in enumerate(file_list_sorted):
            if i % 2 == 0:
                self.clips.append(
                    self.generate_image(
                        image_path=item,
                        duration=TIME_IMAGE_SMALL,
                        start_time=i,
                        image_height=480,
                        image_width=640,
                        horizontal_pos="left",
                        vertical_pos="bottom"
                    )
                )
            else:
                self.clips.append(
                    self.generate_image(
                        image_path=item,
                        duration=TIME_IMAGE_SMALL,
                        start_time=i, 
                    )
                )
        self.clip = CompositeVideoClip(self.clips, size=(SCREEN_HEIGHT, SCREEN_WIDTH))

    def add_audio_to_video(self, audio_file_path):
        """
            add audio from filepath to current video file
        """
        audioclip = AudioFileClip(audio_file_path)
        audioclip = audioclip.set_duration(self.clip.duration)
        self.clip.audio = audioclip

    def write_final_clip(self, output_file_path, FPS):
        """
            write videoclip
        """
        self.clip.write_videofile(output_file_path, fps=FPS)

