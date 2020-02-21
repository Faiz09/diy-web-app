import pytest

class TestPosts:
    def test_create_posts(self):
        assert 1==1

    @pytest.mark.live
    def test_update_posts(self):
        assert 'x' == 'x'

