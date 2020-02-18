from werkzeug import Request


class PostController:
    def __init__(self):
        pass

    def show_post(self, req: Request, id):
        return 'CC..'

    def show_something_else(self, req: Request, id, spam):
        return 'DD..'