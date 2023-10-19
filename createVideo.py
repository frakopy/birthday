from moviepy.editor import ImageClip, AudioFileClip
import os
from PIL import Image

current_directory =  os.path.dirname(__file__)


# Load the image
image_path = os.path.join(current_directory, "images" ,"papa.jpg")
# Correct the image orientation
image = Image.open(image_path)
image = image.transpose(Image.Transpose.ROTATE_270)  # Adjust the rotation angle as needed
image.save(os.path.join(current_directory, "images" ,"papa.jpg"))

image_clip = ImageClip(image_path, duration=4)  # Adjust the duration as needed

# Load the audio
audio_path = os.path.join(current_directory, "audios" ,"papa.mp3")
audio_clip = AudioFileClip(audio_path)  # Adjust the audio file path as needed

# Set the audio for the image clip
video_clip = image_clip.set_audio(audio_clip)

# Write the video to a file
final_path = os.path.join(current_directory, "videos" ,"video_papa.mp4")
video_clip.write_videofile(final_path, codec="libx264", fps=24)  # Adjust codec and frame rate as needed
