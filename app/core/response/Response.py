import json


class Response:
    def __init__(self):
        pass

    @staticmethod
    def success(data={}, code=200):
        return json.dumps({
            'data': data,
            'code': code
        })

    @staticmethod
    def error(message='', code=500):
        return json.dumps({
            'message': message,
            'code': code
        })