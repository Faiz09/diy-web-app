from app.user.model.user import User
from app.post.model.post import Post
from app.core.dispatchers.dispatcher import Dispatcher


class DeleteUser(Dispatcher):
    user_id = None
    user = None

    def __init__(self, user_id):
        self.user = User()
        self.user_id = user_id

    def handle(self):
        deleting_user = User().find(self.user_id)
        for post in deleting_user.posts:
            Post().delete_by_id(post.id)

        return self.user.delete_by_id(self.user_id)

