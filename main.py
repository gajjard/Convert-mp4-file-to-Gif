# use "pip install moviepy" to install Moviepy library.
# Import moviepy.editor
from moviepy.editor import *

# Taking video as an input which we want to convert in GIF.
video_input = VideoFileClip("Countdown.mp4")

# converting video file to GIF.
video_input.write_gif("output.gif")

