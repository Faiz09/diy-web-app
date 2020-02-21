import pytest

from app.post.model.post import Post
from app.user.model.user import User


class TestUserPost:

    @pytest.mark.live
    def test_user_post(self):
        u = User(first_name='John', last_name='Kennedy', email='president@america.com')
        u.posts.append(
            Post(title='A country', body='A government should have prinicples')
        )
        u.create()

        assert isinstance(u, User)
        assert u.email == 'president@america.com'
        assert isinstance(u.posts[0], Post)
        assert u.posts[0].user_id == u.id
