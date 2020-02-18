from werkzeug import Request
import json


class CoreController:
    def __init__(self):
        pass

    def welcome(self, req: Request):
        return json.dumps({
            'message': 'welcome',
        })