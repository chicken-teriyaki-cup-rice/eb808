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


def test_framework_test_client_can_send_requests(api, test_client):
    RESPONSE_TEXT = "Hello World!"

    @api.route("/hey")
    def hey(req, resp):
        resp.text = RESPONSE_TEXT

    assert test_client.get("http://testserver/hey").text == RESPONSE_TEXT
