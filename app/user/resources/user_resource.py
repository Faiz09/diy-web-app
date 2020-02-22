from app.user.model.user import User
from app.post.resources.post_resource_collection import PostResourceCollection


class UserResource:
    user = None

    def __init__(self, user: User):
        self.user = user

    def data(self):
        return {
            'id': self.user.id,
            'first_name': self.user.first_name,
            'posts': PostResourceCollection(self.user.posts).data(),
        }