#! /usr/bin/env python3

from werkzeug.routing import Rule
from server.server import Server
from cli.cli import Cli
from database.migrate import DatabaseMigration

# We are lunching the app here, giving a pretty good idea how things starts and where they lead to


def lunch_app():
    Server([
        Rule('/', methods=['GET'], endpoint='HomeController.index'),
        Rule('/<id>', methods=['GET'], endpoint='PostController.show_post'),
        Rule('/<id>/<spam>', methods=['GET'], endpoint='PostController.show_something_else'),
    ]).run()


# We also need some housekeeping - like app setting, database migration, seeders etc
# we will abstract them away...

if __name__ == '__main__':
    args = Cli().listen()

    if args.m is not False:
        migrations = DatabaseMigration()
        if args.m == 'up':
            migrations.up()
            exit('\nMigrated schema..\n')
        if args.m == 'down':
            migrations.down()
            exit('\nRolled back migrations..\n')

    else:
        lunch_app()



