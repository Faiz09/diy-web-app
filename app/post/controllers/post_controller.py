from werkzeug import Request
from app.core.response.Response import Response
from app.post.model.post import Post
from app.post.resources import PostResource, PostResourceCollection
from app.core.controllers import CoreController
from app.post.dispatchers import CreatePost, UpdatePost, DeletePost


class PostController(CoreController):
    def __init__(self):
        super().__init__()

    def index(self, req: Request):
        return Response.success(
            PostResourceCollection(Post().all()).data()
        )

    def show(self, req: Request, id):
        return Response.success(
            PostResource(self.find(Post(), id)).data()
        )

    def update(self, req: Request, id):
        post = self.find(Post(), id)
        post = UpdatePost(id, req.form.to_dict()).handle()
        return Response.success(
            PostResource(post).data()
        )

    def store(self, req: Request):
        post = CreatePost(req.form.to_dict()).handle()
        return Response.success(
            PostResource(post).data()
        )

    def delete(self, req: Request, id):
        post = self.find(Post(), id)
        DeletePost(id).handle()
        return Response.success(message='{} resouce with {} deleted'.format(type(post).__name__, id))