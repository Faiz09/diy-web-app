from werkzeug import Request
from app.core.response.Response import Response
from app.user.model.user import User
from app.user.resources import UserResourceCollection, UserResource
from app.core.controllers import CoreController
from app.user.dispatchers import CreateUser, UpdateUser, DeleteUser


class UserController(CoreController):
    def __init__(self):
        super().__init__()

    def index(self, req: Request):
        return Response.success(
            UserResourceCollection(User().all()).data()
        )

    def show(self, req: Request, id):
        return Response.success(
            UserResource(self.find(User(), id)).data()
        )

    def update(self, req: Request, id):
        user = self.find(User(), id)
        user = UpdateUser(id, req.form.to_dict()).handle()
        return Response.success(
            UserResource(user).data()
        )

    def store(self, req: Request):
        user = CreateUser(req.form.to_dict()).handle()
        return Response.success(
            UserResource(user).data()
        )

    def delete(self, req: Request, id):
        user = self.find(User(), id)
        DeleteUser(id).handle()
        return Response.success(message='{} resouce with {} deleted'.format(type(user).__name__, id))
