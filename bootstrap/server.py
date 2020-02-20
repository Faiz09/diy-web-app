import os

from werkzeug import Response, Request
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.routing import Map
from werkzeug.serving import run_simple
from routes import routes
from werkzeug.exceptions import NotFound


class Server:
    map = None

    def __init__(self):
        self.map = Map(self.load_routes())

    def handle(self, environ, start_response):
        request = Request(environ)
        endpoint, values = self.map.bind_to_environ(request.environ).match()
        return Response(endpoint(request, **values))(environ, start_response)

    def run(self):
        run_simple('127.0.0.1', 5000, SharedDataMiddleware(self.handle, {
            '/static': os.path.join(os.path.dirname(__file__) + "/../", 'static')
        }), use_debugger=True, use_reloader=True)

    def load_routes(self):
        return routes
