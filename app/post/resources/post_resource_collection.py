from app.post.resources.post_resource import PostResource


class PostResourceCollection:
    posts = None

    def __init__(self, posts: list):
        self.posts = posts

    def data(self):
        posts_list = []
        for post in self.posts:
            posts_list.append(
                PostResource(post).data()
            )

        return posts_list
