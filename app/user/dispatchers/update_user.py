from app.user.model.user import User
from app.core.dispatchers.dispatcher import Dispatcher


class UpdateUser(Dispatcher):
    data = None
    user_id = None
    user = None

    def __init__(self, user_id,  data):
        self.data = data
        self.user = User()
        self.user_id = user_id

    def handle(self):
        return self.user.update(User.id, self.user_id, self.data)

