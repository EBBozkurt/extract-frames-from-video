from PIL import Image
import imagehash
import os


def find_duplicate_images(folder_path: str, image_hashes: dict, duplicate_frames: dict, threshold: int):
    """
    Finds and deletes duplicated or similar frames in given folder.

    Args:
        folder_path (str): The folder path of frames.
        image_hashes (dict): Hash values of frames.
        duplicate_frames (dict): Duplicate frames data of removed frames. If none is deleted, it is empty.
        threshold (int): Threshold value for difference between frames. 0 for duplicated.

    Returns:
        duplicate_frames: Removed duplicated frames from the frame_list.
    """

    # Create a dictionary to store removed frames.
    removed_frames = []

    # Check to find the duplicates.
    if threshold == 0:

        try:

            # Hold each frame.
            for key, value in list(image_hashes.items()):

                # Check if the frame is not removed.
                if key not in removed_frames:

                    # Loop through all frames on holded frame.
                    for k, v in list(image_hashes.items()):

                        # Check if the frame is not removed.
                        if k not in removed_frames:

                            # Pass if the frames are same
                            if not k == key:

                                # If the hash values are the same.
                                if v == value:

                                    # Create image path
                                    image_path = os.path.join(folder_path, k)

                                    # Remove the image from the folder.
                                    os.remove(image_path)

                                    # Append the removed frames into the removed_frames array.
                                    removed_frames.append(k)

                                    # Add removed duplicate frame into the dictionary created for duplicate and main frames.
                                    duplicate_frames.setdefault(
                                        key, []).append(k)

                                    print(f"Removed duplicated image: {k}")

            # Return created dictionary.
            return duplicate_frames

        except Exception as e:

            print("An Exception has occured while deleting duplicates: ", e)

    # To find and delete similar frames according to the given threshold.
    else:

        try:

            # Hold each frame.
            for key, value in list(image_hashes.items()):

                # Check if the frame is not removed.
                if key not in removed_frames:

                    # Loop through all frames on holded frame.
                    for k, v in list(image_hashes.items()):

                        # Check if the frame is not removed.
                        if k not in removed_frames:

                            # Pass if the frames are same
                            if not k == key:

                                # If the hash value is smaller than the threshold(difference).
                                if v-value <= threshold:

                                    # Create image path
                                    image_path = os.path.join(folder_path, k)

                                    # Remove the image.
                                    os.remove(image_path)

                                    # Append the removed frames into the removed_frames array.
                                    removed_frames.append(k)

                                    # If the holded frame has removed duplicates.
                                    if key in duplicate_frames:

                                        # Append the similar frame into the holded frame's duplicates.
                                        duplicate_frames[key].append(k)

                                        # If similar frame has any removed duplicate images.
                                        if k in duplicate_frames:

                                            # Add the similar frame's duplicates into the holded frame.
                                            duplicate_frames[key].extend(
                                                duplicate_frames[k])

                                    # If the holded frame does not have any removed duplicated frame.
                                    elif key not in duplicate_frames:

                                        # Add the frame into the dict and it's similar frame.
                                        duplicate_frames.setdefault(
                                            key, []).append(k)

                                        # If the similar frame has removed duplicated frame in
                                        if k in duplicate_frames:

                                            # Add  the removed similar frame's duplicated frames.
                                            duplicate_frames[key].extend(
                                                duplicate_frames[k])

                                    print(f"Removed similar image: {k}")

            # Retrun the deuplicated frames dict.
            return duplicate_frames

        except Exception as e:

            print("An Exception has occured while deleting duplicates: ", e)


def compute_hashes(folder_path: str):
    """
    Computes each frames hash value.

    Args:
        folder_path (str) : Folder path of frames.

    Returns:
        image_hashes (dict) : Includes each frames hash value.
    """

    image_hashes = {}

    try:
        # Loop through each image.
        for image_file in os.listdir(folder_path):

            # Check if the file is image.
            if not image_file.endswith(".ini"):

                # Create the image path
                image_path = os.path.join(folder_path, image_file)

                # Open the image.
                with Image.open(image_path) as image:

                    # Calculate the hash value of the image.
                    image_hash = imagehash.average_hash(image, hash_size=8)

                    # Add hash value into the dictionary with the image file name as key.
                    image_hashes[image_file] = image_hash

        # Return the created dictionary.
        return image_hashes

    except Exception as e:

        print(
            "An exception has occurred while computing the hash values of the frames: ", e)


def create_similar_locations(input_dict):

    output_dict = {}

    try:

        # Loop through each frame in dict.
        for key, values in input_dict.items():

            # Recreate the dictionary.
            split_values = [value.split('_')[-1].split('.')[0]
                            for value in values]
            split_values = str(split_values).replace(',', '|').replace(
                '[', '').replace(']', '').replace("'", "")
            output_dict[key] = split_values

        # Return created dictionary.
        return output_dict

    except Exception as e:

        print("An exception has ocuured while creating the similar_locations variable: ", e)


def remove_duplicates_similar_frames(folder_path: str):
    """
    Calls functions for the process of removing duplicated and similar frames.

    Args:
        folder_path (str) : The folder path of the frames.

    Returns:
        duplicate_images (dict) : Returns frames' duplicated and similar frames dictionary.

    """

    # Create a dictionary to add the frame's similar and duplicated frames.
    duplicate_images = {}

    # Calculate each frame's hash values.
    image_hashes = compute_hashes(folder_path)

    # Removes the duplicates and similar of the images.
    find_duplicate_images(
        folder_path, image_hashes, duplicate_images, 5)

    # Calculate each frame's hash values after the deletion.
    # image_hashes = compute_hashes(folder_path)

    # Find and remove the similar images according to the given threshold value.
    # duplicate_images = find_duplicate_images(folder_path, image_hashes, duplicate_images, 7)

    # Create the similar locations format
    # duplicate_images = create_similar_locations(duplicate_images)

    # Return the duplicated and similar images data.
    return duplicate_images
