from werkzeug import Request
from app.core.response.Response import Response
from app.user.model.user import User
from app.user.resources.user_resource_collection import UserResourceCollection


class UserController:
    def __init__(self):
        pass

    def index(self, req: Request):
        return Response.success(
            UserResourceCollection(User().all()).data()
        )
