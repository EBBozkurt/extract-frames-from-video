import os
import shutil


def get_input_video_path() -> str:
    """
    Prompt the user to enter the path of the input video file, and return the path.

    Returns:
        str: The path of the input video file entered by the user.
    """
    while True:
        # Prompt the user to enter the path of the input video file.
        input_path = input('Enter input video path: ')

        # Check if the file path is valid.
        if os.path.exists(input_path):
            # If the file path is valid, break out of the loop.
            break
        else:
            # If the file path is not valid, print an error message and continue the loop.
            print(
                f"Error: '{input_path}' is not a valid file path. Please try again.")

    # Return the input video file path entered by the user.
    return input_path


def get_output_folder_path() -> str:
    while True:
        # Prompt the user to enter the name of the output folder.
        output_folder_path = input("Enter the path of the output folder: ")

        # Check if the folder name already exists.
        if not os.path.exists(output_folder_path):
            print(
                f"Error: '{output_folder_path}' is not exists. Please check.")
            # Clear the wrong given output_folder_path
            output_folder_path = ""
        else:
            break

    # Return the output folder name entered by the user.
    return output_folder_path


def read_integer(prompt: str) -> int:
    """
    Prompts the user to enter an integer and returns the integer value.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        int: The integer value entered by the user.
    """
    while True:
        value_str = input(prompt)
        if value_str.isdigit():
            return int(value_str)
        else:
            print("Invalid input. Please enter an integer value.")


def move_extracted_frames(source_dir: str, target_dir: str):
    file_names = os.listdir(source_dir)

    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)
