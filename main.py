from werkzeug.routing import Rule
from server.server import Server

Server([
    Rule('/', methods=['GET'], endpoint='HomeController.index'),
    Rule('/<id>', methods=['GET'], endpoint='PostController.show_post'),
    Rule('/<id>/<spam>', methods=['GET'], endpoint='PostController.show_something_else'),
]).run()
