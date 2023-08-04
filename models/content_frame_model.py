import json

class ContentFrameIndex:
    CONTENT_ID: int
    FILENAME: str
    FOLDERURL: str
    LOCATION: str
    SIMILAR_LOCATIONS: str or None

    def __init__(self, CONTENT_ID: int, FILENAME: str, FOLDERURL: str, LOCATION: str, SIMILAR_LOCATIONS: str) -> None:
        self.CONTENT_ID = CONTENT_ID
        self.FILENAME = FILENAME
        self.FOLDERURL = FOLDERURL
        self.LOCATION = LOCATION
        self.SIMILAR_LOCATIONS = SIMILAR_LOCATIONS


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ContentFrameIndex):
            return {
                "CONTENT_ID": obj.CONTENT_ID,
                "FILENAME": obj.FILENAME,
                "FOLDERURL": obj.FOLDERURL,
                "LOCATION": obj.LOCATION,
                "SIMILAR_LOCATIONS": obj.SIMILAR_LOCATIONS
            }
        return super().default(obj)
