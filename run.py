#! /usr/bin/env python3

from bootstrap.server import Server
from bootstrap.cli import Cli
from database.seeder.seeder import Seeder

if __name__ == '__main__':
    args = Cli().listen()

    if args.s is not False:
        Seeder().seed()
    else:
        Server().run()


