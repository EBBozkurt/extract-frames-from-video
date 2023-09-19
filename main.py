import os
import tempfile
import sys
from global_functions.appConstant import content_persona_ai_drive_url
from global_functions.Enums import EnumContentRowStates
from global_functions.send_to_db import get_content_list_by_content_id, get_content_list_by_state, update_content_rowState
from services.duplicate import remove_duplicate_similar_frames
from services.file import move_extracted_frames, read_integer
from services.video import extract_frames, open_video

def main(threshold_value):
    while True:
        # Create a temporary directory to work with
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Fetch content information from the database
            target_row_state_wfa = EnumContentRowStates.WaitingForAnalysis.value
            wfa_content_list = get_content_list_by_state(target_row_state_wfa)
            if wfa_content_list:
                content = wfa_content_list[0]
                content_id = content.ID
                starting_frame = 0
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
    print(sys.argv)
    if len(sys.argv) != 2:
        # Print usage instructions if incorrect number of arguments provided
        print("Usage: python main.py threshold_value")
    else:
        # Convert command-line arguments to appropriate data types
        threshold_value = int(sys.argv[1])
        # Call the main function with the provided arguments
        main(threshold_value)
