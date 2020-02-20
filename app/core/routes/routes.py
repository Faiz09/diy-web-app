from werkzeug.routing import Rule
from app.core.controllers.core_controller import CoreController

home_routes = [
    Rule('/', endpoint=CoreController().welcome),
]