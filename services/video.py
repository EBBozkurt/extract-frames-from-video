import datetime
import cv2
import os
import time

from global_functions.progress_indicator import progress_inditacor
from global_functions.send_to_db import update_video_resolution


def open_video(input_path: str) -> cv2.VideoCapture:
    """
    Open a video file from the given input path using OpenCV's VideoCapture function.

    Args:
        input_path (str): The path of the video file to be opened.

    Returns:
        cv2.VideoCapture: The VideoCapture object that represents the opened video file.
    """
    try:
        # Try to open the video file using OpenCV's VideoCapture function.
        video = cv2.VideoCapture(input_path)
    except:
        # If there's an error opening the file, print an error message and exit the program.
        print(
            f"Error: could not open '{input_path}'. Please ensure that the file path is valid and try again.")
        exit()

    # Return the VideoCapture object that represents the opened video file.
    return video


def extract_frames(video:  cv2.VideoCapture, output_folder_path: str, content_id: int, starting_frame: int) -> None:
    """
    Extract the frames from the video and save them as image files in the output folder.

    Args:
        video (cv2.VideoCapture): The input video object.
        output_folder_path (str): The name of the output folder to store the extracted frames.
    """

    # Start the timer
    start_time = time.time()
    print('The extracting process has been started... Please wait...')

    # Initialize a frame counter
    frame_count = 0

    # Get video total frame count
    total_frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Loop through the video frames
    while True:
        # Read a frame from the video
        # In the OpenCV library, [ret] is a boolean variable that is used to indicate whether the read() method was successful or not.
        ret, frame = video.read()

        # If the frame is not valid, exit the loop
        if not ret:
            break

        # Start Progress Indicator
        progress_inditacor(frame_count, total_frame_count, "extract_frames")

        # Get the timestamp of the current frame in milliseconds
        timestamp = video.get(cv2.CAP_PROP_POS_MSEC)

        # Convert timestamp to a datetime object
        timestamp_delta = datetime.timedelta(milliseconds=timestamp)

        # Extract hours, minutes, seconds and milliseconds from the delta object
        hours, remainder = divmod(timestamp_delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = timestamp_delta.microseconds // 1000

        # Format the datetime object as a string in the format "hour-minute-second-millisecond"
        timestamp_str = f"{hours:02d}-{minutes:02d}-{seconds:02d}-{milliseconds:03d}"

        # Save the frame as an image file with a unique name in the output folder, Ex:
        # "cid_2_fr_25_ts_00-00-35-023"
        file_name = f"cid_{content_id}_fr_{frame_count}_ts_{timestamp_str}"

        file_path = os.path.join(
            output_folder_path, f'{file_name}.jpg')

        if (starting_frame <= frame_count):
            cv2.imwrite(file_path, frame)

        # Increment the frame counter
        frame_count += 1

    # Stop the timer
    end_time = time.time()

    # Calculate the processing time of the while loop
    processing_time = end_time - start_time
    processing_time = "{:.2f}".format(processing_time)

    # Print the processing time
    print(
        f'The video has been processed. Total frames: {frame_count}. Processing time: {processing_time} seconds.')

    # Update video resolution
    # Get the resolution (width and height) of the video
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    update_video_resolution(content_id, width, height)
    # Print the processing time
    print(
        f'The video has been updated. Width: {width}. Height: {height}.')
