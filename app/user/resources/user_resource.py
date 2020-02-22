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
            'last_name': self.user.last_name,
            'email': self.user.email,
            'created_at': self.user.created_at.strftime("%Y-%m-%d %H:%M"),
            'updated_at': self.user.updated_at.strftime("%Y-%m-%d %H:%M"),
            'posts': PostResourceCollection(self.user.posts).data(),
        }