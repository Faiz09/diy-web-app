from models.user import User
from models.post import Post


class DatabaseMigration():
    user = None
    post = None

    def __init__(self):
        self.user = User()
        self.post = Post()

    def up(self):
        self.user.metadata.create_all(self.user.engine())
        self.post.metadata.create_all(self.post.engine())

    def down(self):
        self.user.metadata.drop_all(self.user.engine())
        self.post.metadata.drop_all(self.post.engine())