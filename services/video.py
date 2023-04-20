import cv2
import os
import time
from multiprocessing import Process, queues


def open_video(input_path: str):
    # Open the video file
    try:
        video = cv2.VideoCapture(input_path)
    except:
        print(
            f"Error: could not open '{input_path}'. Please ensure that the file path is valid and try again.")
        exit()

    return video


def extract_frames(video, output_folder_name: str):
    # Extract Frames..
    # Start the timer
    start_time = time.time()
    print('The extracting process has been started... Please wait...')

    # Initialize a frame counter
    # We initialize a frame_count variable to keep track of the number of frames we have processed.
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
        file_path = os.path.join(output_folder_name, f'{output_folder_name}_frame_{frame_count}.jpg')
        cv2.imwrite(file_path, frame)

        # Increment the frame counter
        frame_count += 1

    # Stop the timer
    end_time = time.time()

    # Calculate the processing time of the while loop
    processing_time = end_time - start_time
    processing_time = "{:.2f}".format(processing_time)

    print(f'The video processed within {processing_time} seconds.')
