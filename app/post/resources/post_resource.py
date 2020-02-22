from app.post.model.post import Post


class PostResource:
    post = None

    def __init__(self, post: Post):
        self.post = post

    def data(self):
        return {
            'id': self.post.id,
            'title': self.post.title,
            'body': self.post.body,
            'created_at': self.post.created_at.strftime("%Y-%m-%d %H:%M"),
            'updated_at': self.post.updated_at.strftime("%Y-%m-%d %H:%M"),
        }