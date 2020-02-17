from app.models.user import User
from app.models.post import Post
from app.core.helpers.time import Time


class Seeder:
    def __init__(self):
        pass

    def seed(self):
        return user_posts()


def user_posts():
    user = User(first_name='Wendy', last_name='Williams', email='windy@gmail.com').create()

    user.posts.append(
        Post(title='Hello World', body='A post created by windy, We have to define a relation', created_at=Time().now(), updated_at=Time().now())
    )

    return user
