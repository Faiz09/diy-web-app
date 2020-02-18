from database.seeder.user_post_seeder import UserPostSeeder

class Seeder:
    def __init__(self):
        pass

    def seed(self):
        UserPostSeeder(copies=100).run()
