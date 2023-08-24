import json
from models.content_frame_model import CustomEncoder
from models.content_model import Content
from services.http import send_post_request


def send_frames_to_db(frame_list: list):
    url = "PostContentFrameIndexList"

    body = {"FRAMELIST": frame_list}

    send_post_request(url, json.dumps(body, cls=CustomEncoder))

def update_content_rowState(content_id: int, target_row_state: int):
    body = {
        "ContentID": content_id,
        "RowState": target_row_state
      }
    url = "UpdateContentRowState"
    response_data = send_post_request(url, json.dumps(body, cls=CustomEncoder))
    return response_data

def update_video_resolution(ContentID: int, Width: int,Height: int ):
    body = {
        "ContentID": ContentID,
        "Width": Width,
        "Height": Height,
      }
    url = "UpdateContentResolution"
    response_data = send_post_request(url, json.dumps(body, cls=CustomEncoder))
    return response_data