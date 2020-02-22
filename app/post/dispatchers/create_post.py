from app.post.model.post import Post
from app.user.model.user import User
from app.core.dispatchers.dispatcher import Dispatcher
from app.core.exceptions.exceptions import ResourceNotFoundException


class CreatePost(Dispatcher):
    data = None
    post = None

    def __init__(self, data):
        self.data = data
        self.post = Post()

    def handle(self):
        user = self.get_user()
        post = self.fill(self.post, self.data).create()
        self.bind_to_user(user, post)
        return post

    def get_user(self):
        if 'user' not in self.data:
            raise ResourceNotFoundException(message='')

        user = User().find(self.data['user'])

        if user is None:
            raise ResourceNotFoundException(message='User doesnt exists')

        return user

    def bind_to_user(self, user: User, post: Post):
        Post().update(Post.id, post.id, {'user_id': user.id})

