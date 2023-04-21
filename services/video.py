import cv2
import os
import time


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


def extract_frames(video:  cv2.VideoCapture, output_folder_name: str) -> None:
    """
    Extract the frames from the video and save them as image files in the output folder.

    Args:
        video (cv2.VideoCapture): The input video object.
        output_folder_name (str): The name of the output folder to store the extracted frames.
    """
    # Start the timer
    start_time = time.time()
    print('The extracting process has been started... Please wait...')

    # Initialize a frame counter
    frame_count = 0

    # Loop through the video frames
    while True:
        # Read a frame from the video
        # In the OpenCV library, [ret] is a boolean variable that is used to indicate whether the read() method was successful or not.
        ret, frame = video.read()

        # If the frame is not valid, exit the loop
        if not ret:
            break

        # Save the frame as an image file with a unique name in the output folder
        file_path = os.path.join(
            output_folder_name, f'{output_folder_name}_frame_{frame_count}.jpg')
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
