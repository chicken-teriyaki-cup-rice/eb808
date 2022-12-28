import pytest

from api import API


def test_basic_route_adding(api):
    @api.route("/home")
    def home(req, resp):
        resp.text = "Hello World!"


def test_route_adding_with_same_path(api):
    @api.route("/home")
    def home(req, resp):
        resp.text = "Hello World!"

    with pytest.raises(AssertionError):

        @api.route("/home")
        def home2(req, resp):
            resp.text = "Hello World!"


def test_framework_test_client_can_send_requests(api, client):
    RESPONSE_TEXT = "Hello World!"

    @api.route("/hey")
    def hey(req, resp):
        resp.text = RESPONSE_TEXT

    assert client.get("http://testserver/hey").text == RESPONSE_TEXT


def test_parameterized_route(api, client):
    @api.route("/{name}")
    def hello(req, resp, name):
        resp.text = f"It's {name}!"

    assert client.get("http://testserver/pikachu").text == "It's pikachu!"
    assert client.get("http://testserver/snorlax").text == "It's snorlax!"


def test_default_404_response(client):
    response = client.get("http://testserver/doesnotexist")
    assert response.status_code == 404
    assert response.text == "Not found."


def test_class_based_handler_get(api, client):
    response_text = "this is a get request"

    @api.route("/plant")
    class PlantResource:
        def get(self, req, resp):
            resp.text = response_text

    assert client.get("http://testserver/plant").text == response_text


def test_class_based_handler_post(api, client):
    response_text = "this is a post request"

    @api.route("/plant")
    class PlantResource:
        def post(self, req, resp):
            resp.text = response_text

    assert client.post("http://testserver/plant").text == response_text


def test_class_based_handler_not_allowed_method(api, client):
    @api.route("/plant")
    class PlantResource:
        def post(self, req, resp):
            resp.text = "yolo"

    with pytest.raises(AttributeError):
        client.get("http://testserver/plant")


def test_alternative_route(api, client):
    response_text = "Alternative way to add a route"

    def home(req, resp):
        resp.text = response_text

    api.add_route("/alternative", home)

    assert client.get("http://testserver/alternative").text == response_text


def test_template(api, client):
    @api.route("/html")
    def html_handler(req, resp):
        resp.body = api.template(
            "index.html", context={"title": "Some Title", "name": "Some Name"}
        ).encode()

    response = client.get("http://testserver/html")

    assert "text/html" in response.headers["Content-Type"]
    assert "Some Title" in response.text
    assert "Some Name" in response.text


def test_custom_exception_handler(api, client):
    def on_exception(req, resp, exc):
        resp.text = "AttributeErrorHappened"

    api.add_exception_handler(on_exception)

    @api.route("/")
    def index(req, resp):
        raise AttributeError()

    response = client.get("http://testserver/")

    assert response.text == "AttributeErrorHappened"
