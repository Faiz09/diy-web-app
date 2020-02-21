from app.user.model.user import Post
import pytest

class TestPostsClass:

    @pytest.mark.live
    def test_create_posts(self):
        p = Post(title='A hello world post', body='Body goes here')
        p = p.create()
        assert isinstance(p, Post)

    @pytest.mark.live
    def test_where_posts(self):
        u = Post().where(Post.title, 'A hello world post').first()
        assert u.title == 'A hello world post'
        assert isinstance(u, Post)

    @pytest.mark.live
    def test_update_posts(self):
        u = Post().update(Post.title, 'A hello world post', {
            Post.body: 'The body will be changed after this..'
        })
        assert isinstance(u, Post)
        assert u.body == 'The body will be changed after this..'

    @pytest.mark.live
    def test_get_post(self):
        p = Post().where(Post.title, 'A hello world post').first()
        p = Post().find(p.id)
        assert isinstance(p, Post)
        assert p.title == 'A hello world post'

    @pytest.mark.live
    def test_delete_post(self):
        p = Post().where(Post.title, 'A hello world post').first()
        p = Post().delete_by_id(p.id)
        assert p == 1

