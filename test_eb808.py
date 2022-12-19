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


def test_class_based_handler_get(api, client):
    response_text = "this is a get request"

    @api.route("/plant")
    class PlantResource:
        def get(self, req, resp):
            resp.text = response_text

    assert client.get("http://testserver/plant").text == response_text
