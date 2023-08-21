import tempfile
from services.duplicate import remove_duplicate_similar_frames
from services.file import get_input_video_path, get_output_folder_path, move_extracted_frames, read_integer
from services.video import extract_frames, open_video


# Take input video path from user
input_path = get_input_video_path()

# Open the video file
video = open_video(input_path)

# Get the output folder name from the user
output_folder_path = get_output_folder_path()

# Get the content_id for post request
content_id = read_integer(
    'Enter content_id value (You can find that id in docs): ')

# Get the starting frame
starting_frame = read_integer(
    'Enter start frame (If you want to start from beginning please enter zero): ')

# Get the Treshold Value
treshold_value = read_integer(
    'Enter a treshold value for finding similar and duplicate images: ')

# In this part, we create a temp folder and after we do our operations in it, we pass it to our real folder that we got from the user.
with tempfile.TemporaryDirectory() as tmp_dir:

    # Extract Frames..
    extract_frames(video, tmp_dir, content_id, starting_frame)

    # Release the video file to free up system resources
    video.release()

    # Find and remove duplicated and similar frames.
    remove_duplicate_similar_frames(
        output_folder_path, tmp_dir, treshold_value)

    # At the end of the process, we move the remaining frames to the folder that the user entered.
    move_extracted_frames(tmp_dir, output_folder_path)
