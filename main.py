from services.file import create_folder, get_input_video_path, get_output_folder_name
from services.video import extract_frames, open_video

# Take input video path from user
input_path = get_input_video_path()

# Open the video file
video = open_video(input_path)

# Get the output folder name from the user
output_folder_name = get_output_folder_name()

# Create the output folder if it doesn't exist
create_folder(output_folder_name)

# Extract Frames..
extract_frames(video, output_folder_name)

# Release the video file to free up system resources
video.release()
