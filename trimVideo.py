from moviepy.editor import VideoFileClip
import os

current_directory =  os.path.dirname(__file__)
video_path = os.path.join(current_directory,"videos" ,"box.mp4")

videoFile = VideoFileClip(video_path)

# Cuting the video
newVideo = videoFile.subclip(t_start=0, t_end=9)

# Save the new video
newVideo.write_videofile(os.path.join(current_directory, "videos", "new_video.mp4"))

# # Convert the new video to gif format
# videoFile.write_gif(os.path.join(current_directory, "videos", "box.gif"))
# videoFile.set_fps(8).write_gif(os.path.join(current_directory, "videos", "box.gif"))

