from app.models.user import User
from app.models.post import Post
from app.core.helpers.time import Time


class Seeder:
    def __init__(self):
        pass

    def seed(self):
        user_seeder()
        post_seeder()


def user_seeder():
    User(name='wendy', fullname='Wendy Williams', nickname='windy').create()


def post_seeder():
    Post(title='Hello World', body='A post created by windy, We have to define a relation', created_at=Time().now()).create()