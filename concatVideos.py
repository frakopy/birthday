from click import argument
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

current_directory =  os.path.dirname(__file__)
video_kin = os.path.join(current_directory, 'videos', 'video_kin.mp4')
video_sophie = os.path.join(current_directory, 'videos', 'video_sophie.mp4')
video_papa = os.path.join(current_directory, 'videos', 'video_papa.mp4')


# List of video file paths to concatenate
video_files = [video_sophie, video_kin, video_papa]  # Add your video file paths

# Load video clips
video_clips = [VideoFileClip(file) for file in video_files]

# Concatenate the video clips horizontally (you can use 'vstack' for vertical concatenation)
concatenated_clip = concatenate_videoclips(video_clips)

# Write the concatenated video to a file
concatenated_clip.write_videofile("finalVideo.mp4")
