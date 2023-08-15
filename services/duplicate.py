from PIL import Image
import imagehash
import os
import json

def remove_duplicate_similar_frames(folder_path : str):
    """
    Delete the duplicate frames in the folder provided
    
    Keyword arguments:
    folder_path : Path of the folder contains frames
    """
    
    # Master frame that referance for comparison of two frames 
    master_frame_number= 0

    # Similar locations dictionary that stores similar location of each master frames
    similar_locations = {}

    # Files list of the folder provided. It is sorted by frame number
    folder = sorted(sorted(os.listdir(folder_path),key=lambda x:int(x[x.rfind("_")+1:x.rfind(".")])))

    for frame_number in range(1,len(folder)):
        # Open the frame file by its location in the list
        current_frame = Image.open(os.path.join(folder_path,folder[frame_number]))

        # Open the master frame file. Initially first frame of the list.
        master_frame = Image.open(os.path.join(folder_path,folder[master_frame_number]))

        # Calculate treshold value using average_hash difference
        treshold = imagehash.average_hash(current_frame)-imagehash.average_hash(master_frame)

        if treshold < 20:

            # If there is no key with that name
            if not (f"{folder[master_frame_number]}" in similar_locations):

                # Create that key
                similar_locations[f"{folder[master_frame_number]}"] = []

                # Append the frame as similar
                similar_locations[f"{folder[master_frame_number]}"].append(folder[frame_number])

            else:
                # If the key exists, append directly
                similar_locations[f"{folder[master_frame_number]}"].append(folder[frame_number])   

            print(f"Treshold value is {treshold}. {folder[frame_number]} deleted.")

            # Remove the frame 
            os.remove(os.path.join(folder_path,folder[frame_number]))
        else:

            # If treshold value is greater than 20, then set the current frame as master frame
            master_frame_number = frame_number

            print(f"Treshold value is {treshold}. {folder[frame_number]} is the new master frame.")

    # Open json file to store similar locations  
    with open("similar_locations.json","w") as file:

        # Add the similar_locations dict to file as json format
        json.dump(
            similar_locations,
            file
        )


    



