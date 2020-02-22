from app.post.model.post import Post


class PostResource:
    post = None

    def __init__(self, post: Post):
        self.post = post

    def data(self):
        return {
            'id': self.post.id,
            'title': self.post.title,
        }