import json
from config import OBJECT_JSON_SEND

sendkeys_data = {
                    "places" : {"first":"Chennai", "second":"Mumbai"}
                 }

fileobj1= open(OBJECT_JSON_SEND, 'w+')
json.dump(sendkeys_data, fileobj1, indent=4)