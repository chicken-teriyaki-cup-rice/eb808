from api import API
from middleware import Middleware

app = API()


@app.route("/home")
def home(request, response):
    response.text = "Hello from the home page"


@app.route("/about")
def about(request, response):
    response.text = "Hello from the about page"


@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello {name}"


@app.route("/sum/{a:d}/{b:d}")
def sum(request, response, a, b):
    total = int(a) + int(b)
    response.text = f"The sum of {a} and {b} is {total}"


@app.route("/template")
def template_handler(req, resp):
    resp.body = app.template(
        "index.html",
        context={
            "name": "eb808",
            "title": "Native Hawaian Ethnobotany Framework",
        },
    ).encode()


@app.route("/exception")
def exception_throwing_handler(request, response):
    raise AssertionError("This handler should not be used.")


@app.route("/plant")
class PlantsHandler:
    def get(self, req, resp):
        resp.text = "Plants Page"

    def post(self, req, resp):
        resp.text = "Endpoint to create a new plant"


def handler(req, resp):
    resp.text = "sample"


app.add_route("/sample", handler)


def custom_exception_handler(request, response, exception_cls):
    response.text = str(exception_cls)


app.add_exception_handler(custom_exception_handler)


class SimpleCustomMiddleware(Middleware):
    def process_request(self, req):
        print("Processing request", req.url)

    def process_response(self, req, res):
        print("Processing response", req.url)


app.add_middleware(SimpleCustomMiddleware)
