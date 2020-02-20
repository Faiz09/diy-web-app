from werkzeug.routing import Rule
from app.post.controllers.post_controller import PostController
from app.core.response.Response import Response

routes = [

    Rule('/post/<id>', endpoint=PostController().show_post),

    Rule('/post/<id>/<spam>', endpoint=PostController().show_something_else),

    Rule('/post/br', endpoint=lambda r: Response.success({
        'purpose': 'This demonstrates lambda function in routes..'
    })),

]