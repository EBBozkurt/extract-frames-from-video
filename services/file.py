import os


def get_input_video_path():
    # Take input video path from user
    while True:
        input_path = input('Enter input video path: ')
        if os.path.exists(input_path):
            break
        else:
            print(
                f"Error: '{input_path}' is not a valid file path. Please try again.")

    return input_path


def get_output_folder_name():
    # Get the output folder name from the user
    while True:
        output_folder_name = input("Enter the name of the output folder: ")
        if not os.path.exists(output_folder_name):
            break
        else:
            print(
                f"Error: '{output_folder_name}' already exists. Please choose a different name.")

    return output_folder_name


def create_folder(output_folder: str):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
