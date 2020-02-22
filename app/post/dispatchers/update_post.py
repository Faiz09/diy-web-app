from app.post.model.post import Post
from app.core.dispatchers.dispatcher import Dispatcher


class UpdatePost(Dispatcher):
    data = None
    post_id = None
    post = None

    def __init__(self, post_id,  data):
        self.data = data
        self.post = Post()
        self.post_id = post_id

    def handle(self):
        return self.post.update(Post.id, self.post_id, self.data)

