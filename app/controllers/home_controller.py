from werkzeug import Request
import json


class HomeController:
    def __init__(self):
        pass

    def index(self, req: Request):

        return json.dumps({
            'hello': 'World',
            'req': 'something else...'
        })