#! /usr/bin/env python3

from werkzeug.routing import Rule
from server.server import Server
from cli.cli import Cli
from database.migrate import DatabaseMigration
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

def run_migrations(option):
    migrations = DatabaseMigration()
    if option == 'up':
        migrations.up()
        exit('\nMigrated schema..\n')
    if option == 'down':
        migrations.down()
        exit('\nRolled back migrations..\n')


def run_seeders():
    return Seeder().seed()


if __name__ == '__main__':
    args = Cli().listen()

    if args.m is not False:
        run_migrations(args.m)
    elif args.s is not None:
        print(run_seeders().id)
    else:
        lunch_app()



