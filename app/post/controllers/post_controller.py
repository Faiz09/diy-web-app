from werkzeug import Request
from app.core.response.Response import Response


class PostController:
    def __init__(self):
        pass

    def show_post(self, req: Request, id):
        return Response.success({
            'id': id
        })

    def show_something_else(self, req: Request, id, spam):
        return Response.success({
            'id': id,
            'spam': spam
        })