import json
from models.content_frame_model import CustomEncoder
from models.content_model import Content
from services.http import post_request_json_list, send_post_request


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


def update_video_resolution(ContentID: int, Width: int, Height: int):
    body = {
        "ContentID": ContentID,
        "Width": Width,
        "Height": Height,
    }
    url = "UpdateContentResolution"
    response_data = send_post_request(url, json.dumps(body, cls=CustomEncoder))
    return response_data


def get_content_list_by_content_id(content_id: int):
    data_to_send = {"ID": content_id}
    api_url = "GetContentList"
    response_data = post_request_json_list(api_url, data_to_send)
    content_list = []

    if response_data:
        for item in response_data:
            content = Content(
                ID=item.get("ID"),
                PARENT_CONTENT_ID=item.get("PARENT_CONTENT_ID"),
                CONTENT_TYPE_ID=item.get("CONTENT_TYPE_ID"),
                NAME_ORIGINAL=item.get("NAME_ORIGINAL"),
                SHORT_INFO_ORIGINAL=item.get("SHORT_INFO_ORIGINAL"),
                ORIGIN_ID=item.get("ORIGIN_ID"),
                RUN_TIME=item.get("RUN_TIME"),
                RELATED_URL=item.get("RELATED_URL"),
                WIDTH=item.get("WIDTH"),
                HEIGHT=item.get("HEIGHT"),
                OPTIME=item.get("OPTIME"),
                rowState=item.get("rowState")
            )
            content_list.append(content)

    return content_list
