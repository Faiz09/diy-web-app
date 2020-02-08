from models.user import User
from models.post import Post
from datetime import datetime

class Seeder:
    def __init__(self):
        pass

    def seed(self):
        user_seeder()
        post_seeder()


def user_seeder():
    User(name='wendy', fullname='Wendy Williams', nickname='windy').create()


def post_seeder():
    Post(title='Hello World', body='A post created by windy, We have to define a relation', created_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')).create()