from app.user.model.user import User
from app.core.dispatchers.dispatcher import Dispatcher


class CreateUser(Dispatcher):
    data = None
    user = None

    def __init__(self, data):
        self.data = data
        self.user = User()

    def handle(self):
        return self.fill(self.user, self.data).create()

