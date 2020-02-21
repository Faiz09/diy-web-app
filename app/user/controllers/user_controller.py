import json
from werkzeug import Request
from app.user.model.user import User


class UserController:
    def __init__(self):
        pass

    def index(self, req: Request):
        return json.dumps({
            'users': User().all().to_json()
        })