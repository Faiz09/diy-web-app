import jsonpickle


class Response:
    def __init__(self):
        pass

    @staticmethod
    def success(data={}, code=200):
        return jsonpickle.encode({
            'data': data,
            'code': code
        })

    @staticmethod
    def error(message='', code=500):
        return jsonpickle.encode({
            'message': message,
            'code': code
        })