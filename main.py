import os
import tempfile
import sys
from global_functions.appConstant import content_persona_ai_drive_url
from global_functions.Enums import EnumContentRowStates
from global_functions.send_to_db import get_content_list_by_content_id, update_content_rowState
from services.duplicate import remove_duplicate_similar_frames
from services.file import move_extracted_frames, read_integer
from services.video import extract_frames, open_video

def main(content_id, starting_frame, threshold_value):
    # Create a temporary directory to work with
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Fetch content information from the database
        content_list = get_content_list_by_content_id(content_id)
        if content_list:
            content = content_list[0]
            # Build the input video path
            input_path = content_persona_ai_drive_url + content.RELATED_URL
            # Open the video file
            video = open_video(input_path)
            # Update the content row state to indicate splitting is in progress
            target_row_state_split = EnumContentRowStates.Splitting.value
            update_content_rowState(content.ID, target_row_state_split)
            # Extract frames from the video
            extract_frames(video, tmp_dir, content_id, starting_frame)
            video.release()  # Release the video file
            # Build the output folder path
            movie_dir = os.path.dirname(input_path)
            output_folder_path = os.path.join(movie_dir, "frames")
            # Remove duplicated and similar frames
            remove_duplicate_similar_frames(output_folder_path, tmp_dir, threshold_value)
            # Move extracted frames to the final folder
            move_extracted_frames(tmp_dir, output_folder_path)
            # Update the content row state to indicate splitting is complete
            target_row_state_splitted = EnumContentRowStates.Splitted.value
            update_content_rowState(content_id, target_row_state_splitted)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        # Print usage instructions if incorrect number of arguments provided
        print("Usage: python main.py content_id starting_frame threshold_value")
    else:
        # Convert command-line arguments to appropriate data types
        content_id = int(sys.argv[1])
        starting_frame = int(sys.argv[2])
        threshold_value = int(sys.argv[3])
        # Call the main function with the provided arguments
        main(content_id, starting_frame, threshold_value)
