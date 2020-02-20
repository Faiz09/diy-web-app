from werkzeug.routing import Rule
from app.user.controllers.user_controller import UserController

user_routes = [
    Rule('/user', endpoint=UserController().index),
]