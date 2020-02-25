import os

CONFIG = {
    'database': {
        'user': 'faiz',
        'password': 'secret',
        'host': 'localhost',
        'database': 'f_py',
    },
    'templates': {
        'path': os.path.join(os.path.dirname(__file__), '../static/templates')
    }
}


def get_templates_path():
    return CONFIG['templates']['path']