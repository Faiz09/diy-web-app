import pytest
from app.user.dispatchers.create_user import CreateUser
from app.user.model.user import User


class TestUsersDispatchers:

    @pytest.mark.live
    def test_user_create_dispatcher(self):
        u = CreateUser({
            'first_name': 'Mark',
            'last_name': 'dice',
            'email': 'mark@doce.com'
        }).handle()

        assert isinstance(u, User)
        assert u.email == 'mark@doce.com'
