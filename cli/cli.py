class Cli:
    def __init__(self):
        pass

    def listen(self):
        import argparse

        parser = argparse.ArgumentParser(description='A DIY web app.')

        parser.add_argument('--r', help='run web app..', default=True, nargs='?')
        parser.add_argument('--m', help='run migrations..', choices=['up', 'down'], default=False, nargs='?')
        parser.add_argument('--s', help='run seeder..', default=False, nargs='?')
        return parser.parse_args()