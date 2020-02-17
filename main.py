#! /usr/bin/env python3

from werkzeug.routing import Rule
from server.server import Server
from cli.cli import Cli
from database.seeder import Seeder
# We are lunching the app here, giving a pretty good idea how things starts and where they lead to

def lunch_app():
    Server([
        Rule('/', methods=['GET'], endpoint='HomeController.index'),
        Rule('/<id>', methods=['GET'], endpoint='PostController.show_post'),
        Rule('/<id>/<spam>', methods=['GET'], endpoint='PostController.show_something_else'),
    ]).run()


# We also need some housekeeping - like app setting, database migration, seeders etc
# we will abstract them away...

def run_seeders():
    return Seeder().seed()


if __name__ == '__main__':
    args = Cli().listen()

    if args.s is not False:
        print(run_seeders().posts)
    else:
        lunch_app()



