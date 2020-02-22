from werkzeug.routing import Rule
from app.user.controllers.user_controller import UserController

routes = [
    Rule('/user', methods=['GET'], endpoint=UserController().index),
    Rule('/user/<id>', methods=['GET'], endpoint=UserController().show),
    Rule('/user/<id>', methods=['PATCH'], endpoint=UserController().update),
    Rule('/user', methods=['POST'], endpoint=UserController().store),
    Rule('/user/<id>', methods=['DELETE'], endpoint=UserController().delete),
]