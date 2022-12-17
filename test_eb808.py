import pytest

from api import API


@pytest.fixture
def api():
    return API()


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
