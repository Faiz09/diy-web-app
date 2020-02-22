from werkzeug.routing import Rule
from app.post.controllers.post_controller import PostController
from app.core.response.Response import Response

routes = [
    Rule('/post', methods=['GET'], endpoint=PostController().index),
    Rule('/post/<id>', methods=['GET'], endpoint=PostController().show),
    Rule('/post/<id>', methods=['PATCH'], endpoint=PostController().update),
    Rule('/post', methods=['POST'], endpoint=PostController().store),
    Rule('/post/<id>', methods=['DELETE'], endpoint=PostController().delete),
    Rule('/post/lambda', methods=['GET'], endpoint=lambda r: Response.success({
        'purpose': 'This demonstrates lambda function in routes..'
    })),

]