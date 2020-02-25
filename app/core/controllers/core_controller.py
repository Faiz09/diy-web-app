from werkzeug import Request
from app.core.exceptions.exceptions import ResourceNotFoundException
from app.core.response.response import Response


class CoreController:
    def __init__(self):
        pass

    def find(self, resource, id):
        res = resource.find(id)
        if res is None:
            raise ResourceNotFoundException(message='{} resource with id:{} doesnt exits.'.format(type(resource).__name__, id))

        return res

    def welcome(self, req: Request):
        return Response.render('home.html', intro='Built in python..', title='A Diy web app!')
