import moviepy.editor as mpe
my_clip = mpe.VideoFileClip('D:\\Work\\BestFIVE\\assets\\1.mp4')
audio_background = mpe.AudioFileClip('D:\\Work\\BestFIVE\\assets\\sound.mp3')
audio_background2 = mpe.AudioFileClip('D:\\Work\\BestFIVE\\assets\\trompeta.mp3')
audio = mpe.afx.audio_loop( audio_background2, duration=my_clip.duration)
final_audio = mpe.CompositeAudioClip([my_clip.audio, audio_background, audio])
final_clip = my_clip.set_audio(final_audio) 
final_clip.set_duration(15).write_videofile("movie.mp4") 
print("e ok")


