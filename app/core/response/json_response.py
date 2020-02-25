class JsonResponse:
    data = None
    headers = None
    mime_type = None

    def __init__(self, data):
        self.data = data
        self.headers = [(
            'Content-type', 'application/json'
        )]
        self.mime_type = 'application/json'

    def send(self):
        return self.data