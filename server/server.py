import sys

from werkzeug import Response, Request
from werkzeug.routing import Map
from werkzeug.serving import run_simple
from exceptions import InvalidMethodException
from controllers.home_controller import HomeController
from controllers.post_controller import PostController


class Server:
    map = None

    def __init__(self, routes):
        self.map = Map(routes)

    def handle(self, environ, start_response):
        request = Request(environ)

        endpoint, values = self.map.bind_to_environ(request.environ).match()

        if not isinstance(endpoint, str):
            raise InvalidMethodException

        endpoint = endpoint.split(".")

        res = getattr(getattr(sys.modules[__name__], endpoint[0])(), endpoint[1])(request, **values)

        response = Response(res)

        return response(environ, start_response)

    def run(self):
        run_simple('127.0.0.1', 5000, self.handle, use_debugger=True, use_reloader=True)