from werkzeug import Response, Request
from werkzeug.routing import Map
from werkzeug.serving import run_simple
from routes import routes


class Server:
    map = None

    def __init__(self):
        self.map = Map(self.load_routes())

    def handle(self, environ, start_response):
        request = Request(environ)

        endpoint, values = self.map.bind_to_environ(request.environ).match()

        return Response(endpoint(request, **values))(environ, start_response)

    def run(self):
        run_simple('127.0.0.1', 5000, self.handle, use_debugger=True, use_reloader=True)

    def load_routes(self):
        return routes
