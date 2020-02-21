from app.user.model.user import User
import pytest

class TestUsersClass:

    @pytest.mark.live
    def test_create_users(self):
        u = User(first_name='John F', last_name='Kennedy', email='john@america.com')
        u = u.create()
        assert isinstance(u, User)

    @pytest.mark.live
    def test_where_users(self):
        u = User().where(User.email, 'john@america.com').first()
        assert isinstance(u, User)

    @pytest.mark.live
    def test_update_users(self):
        u = User().update(User.email, 'john@america.com', {
            User.last_name: 'kennedy'
        })
        assert isinstance(u, User)
        assert u.last_name == 'kennedy' \

    @pytest.mark.live
    def test_get_user(self):
        u = User().where(User.email, 'john@america.com').first()
        u = User().find(u.id)
        assert isinstance(u, User)
        assert u.email == 'john@america.com'

    @pytest.mark.live
    def test_delete_user(self):
        u = User().where(User.email, 'john@america.com').first()
        u = User().delete(u.id)
        assert u == 1

