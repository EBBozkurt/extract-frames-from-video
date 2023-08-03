import os


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


def output_folder_path() -> str:
    """
    Prompt the user to enter the name of the output folder to be created, and return the folder name.

    Returns:
        str: The name of the output folder entered by the user.
    """
    while True:
        # Prompt the user to enter the name of the output folder.
        output_folder_name = input("Enter the name of the output folder: ")

        # Check if the folder name already exists.
        if not os.path.exists(output_folder_name):
            # If the folder name does not exist, break out of the loop.
            break
        else:
            # If the folder name already exists, print an error message and continue the loop.
            print(
                f"Error: '{output_folder_name}' already exists. Please choose a different name.")

    # Return the output folder name entered by the user.
    return output_folder_name


def create_folder(output_folder: str) -> None:
    """
    Create the output folder if it doesn't exist.

    Args:
        output_folder (str): The path of the output folder to be created.
    """
    # Check if the output folder already exists.
    if not os.path.exists(output_folder):
        # If the output folder does not exist, create it using os.makedirs() function.
        os.makedirs(output_folder)
