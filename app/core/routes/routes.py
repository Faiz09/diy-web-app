from werkzeug.routing import Rule
from app.core.controllers.core_controller import CoreController

routes = [
    # do nothing on the goddamn favicon request..
    Rule('/favicon.ico', endpoint=lambda r: None),
    Rule('/', endpoint=CoreController().welcome),
]