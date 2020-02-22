from app.post.model.post import Post
from app.core.dispatchers.dispatcher import Dispatcher


class DeletePost(Dispatcher):
    post_id = None
    post = None

    def __init__(self, post_id):
        self.post = Post()
        self.post_id = post_id

    def handle(self):
        return self.post.delete_by_id(self.post_id)

