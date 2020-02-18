from app.core.helpers.time import Time
from app.user.model.user import User
from app.post.model.post import Post
from faker import Faker
from app.core.console.console import Console
import json


class UserPostSeeder(Console):
    copies = 1
    response = []

    def __init__(self, copies):
        self.copies = copies

    def create(self):

        faker = Faker()

        user = User(first_name=faker.first_name(), last_name=faker.first_name(), email=faker.email())

        user.posts = [
            Post(title=faker.sentence(), body=faker.text(),created_at=Time().now(), updated_at=Time().now()),
            Post(title=faker.sentence(), body=faker.text(),created_at=Time().now(), updated_at=Time().now()),
            Post(title=faker.sentence(), body=faker.text(),created_at=Time().now(), updated_at=Time().now()),
            Post(title=faker.sentence(), body=faker.text(),created_at=Time().now(), updated_at=Time().now()),
            Post(title=faker.sentence(), body=faker.text(),created_at=Time().now(), updated_at=Time().now())
        ]

        self.success(json.dumps(user.create().to_json()))

    def run(self):
        for i in range(self.copies):
            self.create()

        return self.response
