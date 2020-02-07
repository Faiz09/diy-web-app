class InvalidMethodException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.message = 'Method given is invalid.'