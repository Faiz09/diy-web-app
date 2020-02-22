from app.user.resources.user_resource import UserResource


class UserResourceCollection:
    users = None

    def __init__(self, users: list):
        self.users = users

    def data(self):
        users_list = []
        for user in self.users:
            users_list.append(
                UserResource(user).data()
            )

        return users_list