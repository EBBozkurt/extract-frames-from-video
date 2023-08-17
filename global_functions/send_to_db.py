import json
from models.content_frame_model import CustomEncoder
from services.http import send_post_request


def send_frames_to_db(frame_list: list):
    url = "PostContentFrameIndexList"

    body = {"FRAMELIST": frame_list}

    send_post_request(url, json.dumps(body, cls=CustomEncoder))
