from api import API


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


@app.route("/plant")
class PlantsResource:
    def get(self, req, resp):
        resp.text = "Plants Page"

    def post(self, req, resp):
        resp.text = "Endpoint to create a new plant"


def handler(req, resp):
    resp.text = "sample"


app.add_route("/sample", handler)
