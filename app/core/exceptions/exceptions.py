class InvalidUpdateArgumentException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = "Update query requires, {key: '', value: ''} dict as well as data dict"


class InvalidMethodException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = 'Method given is invalid.'


class ResourceNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
