from services.duplicate import remove_duplicate_similar_frames
from services.file import create_folder, get_input_video_path, output_folder_path, read_integer
from services.video import extract_frames, open_video

# Take input video path from user
input_path = get_input_video_path()

# Open the video file
video = open_video(input_path)

# Get the output folder name from the user
output_folder_path_string = output_folder_path()

# Create the output folder if it doesn't exist
create_folder(output_folder_path_string)

# Get the content_id for post request
content_id = read_integer(
    'Enter content_id value (You can find that id in docs): ')

# Get the starting frame
starting_frame = read_integer(
    'Enter start frame (If you want to start from beginning please enter zero): ')

# Extract Frames..
extract_frames(video, output_folder_path_string, content_id, starting_frame)

# Release the video file to free up system resources
video.release()

# Get the Treshold Value
treshold_value = read_integer(
    'Enter a treshold value for finding similar and duplicate images: ')

# Find and remove duplicated and similar frames.
remove_duplicate_similar_frames(output_folder_path_string, treshold_value)
