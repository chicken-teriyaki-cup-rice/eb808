class Middleware:
    def __init__(self, app):
        self.app = app


def add(self, middleware_cls):
    self.app = middleware_cls(self.app)
