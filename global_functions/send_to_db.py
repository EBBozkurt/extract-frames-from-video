def send_frames_to_db(frame_list: list):
    url = "PostContentFrameIndexList"

    body = {"FRAMELIST": frame_list}
    
    print(body)
    #send_post_request(url, json.dumps(body, cls=CustomEncoder))