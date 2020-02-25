import jsonpickle
from app.core.response.json_response import JsonResponse
from app.core.response.view_response import ViewResponse


class Response:
    def __init__(self):
        pass

    @staticmethod
    def success(data={}, message = 'Success', code=200):
        return JsonResponse(jsonpickle.encode({
            'data': data,
            'message': message,
            'code': code
        }))

    @staticmethod
    def error(message='', code=500):
        return JsonResponse(jsonpickle.encode({
            'message': message,
            'code': code
        }))

    @staticmethod
    def render(template='', **context):
        return ViewResponse(template, **context)
