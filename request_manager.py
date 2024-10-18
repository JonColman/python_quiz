from question_request import *

import requests

class RequestManager:
    def __init__(self):
        self.requests = {
            'size': SizeRequest,
            'difficulty': DifficultyRequest,
            'type': TypeRequest,
            'category': CategoryRequest,
        }

    def make_request(self, request_dict):
        request = BaseRequest()
        for type_str, value in request_dict.items():
            request = self.requests[type_str](request, value)
        response = requests.get(str(request))
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve Quiz Questions: {response.status_code}")
            return False
