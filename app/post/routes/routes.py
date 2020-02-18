from werkzeug.routing import Rule
from app.post.controllers.post_controller import PostController

post_routes = [
    Rule('/post/<id>', endpoint=PostController.show_post),
    Rule('/post/<id>/<spam>', endpoint=PostController.show_something_else),
]