from datetime import datetime


class Time:
    def __init__(self):
        pass

    def now(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')