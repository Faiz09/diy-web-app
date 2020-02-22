class Dispatcher:
    def fill(self, resource, data):
        for key in data:
            if key in resource.__dict__:
                setattr(resource, key, data[key])

        return resource
