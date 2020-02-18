from app.core.routes.routes import home_routes as hr
from app.post.routes.routes import post_routes as pr


class Routes:
    routes_lists = None
    final_list = []

    def __init__(self, *routes_lists):
        self.routes_lists = routes_lists
        self.set_routes()

    def set_routes(self):
        for l in self.routes_lists:
            for route in l:
                self.final_list.append(route)

    def get_routes(self):
        return self.final_list


routes = Routes(hr, pr).get_routes()
