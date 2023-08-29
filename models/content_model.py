import json


class Content:
    def __init__(self, ID, PARENT_CONTENT_ID, CONTENT_TYPE_ID, NAME_ORIGINAL, SHORT_INFO_ORIGINAL,
                 ORIGIN_ID, RUN_TIME, RELATED_URL, WIDTH, HEIGHT, OPTIME, rowState):
        self.ID = ID
        self.PARENT_CONTENT_ID = PARENT_CONTENT_ID
        self.CONTENT_TYPE_ID = CONTENT_TYPE_ID
        self.NAME_ORIGINAL = NAME_ORIGINAL
        self.SHORT_INFO_ORIGINAL = SHORT_INFO_ORIGINAL
        self.ORIGIN_ID = ORIGIN_ID
        self.RUN_TIME = RUN_TIME
        self.RELATED_URL = RELATED_URL
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.OPTIME = OPTIME
        self.rowState = rowState


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Content):
            return {
                "ID": obj.ID,
                "PARENT_CONTENT_ID": obj.PARENT_CONTENT_ID,
                "CONTENT_TYPE_ID": obj.CONTENT_TYPE_ID,
                "NAME_ORIGINAL": obj.NAME_ORIGINAL,
                "SHORT_INFO_ORIGINAL": obj.SHORT_INFO_ORIGINAL,
                "ORIGIN_ID": obj.ORIGIN_ID,
                "RUN_TIME": obj.RUN_TIME,
                "RELATED_URL": obj.RELATED_URL,
                "WIDTH": obj.WIDTH,
                "HEIGHT": obj.HEIGHT,
                "OPTIME": obj.OPTIME,
                "rowState": obj.rowState
            }
        return super().default(obj)
