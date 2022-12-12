from parse import parse
from webob import Request, Response

import inspect


class API:
    def __init__(self):
        self.routes = {}

    def __call__(self, environ, start_response):
        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)

    def route(self, path):
        assert path not in self.routes, f"Path {path} already exists."

        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper

    def default_response(self, response):
        response.status_code = 404
        response.text = "Not found."

    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named

        return None, None

    def handle_request(self, request):
        response = Response()

        handler, kwargs = self.find_handler(request_path=request.path)

        if handler is not None:
            if inspect.isclass(handler):
                handler_function = getattr(
                    handler(), request.method.lower(), None
                )
                if handler_function is not None:
                    raise AssertionError("Method not allowed", request.method)
                handler_function(request, response, **kwargs)
            else:
                handler(request, response, **kwargs)
        else:
            self.default_response(response)

        return response
