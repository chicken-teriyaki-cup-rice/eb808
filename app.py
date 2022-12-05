from api import API


app = API()


def home(request, response):
    response.text = "Hello from the home page"


def about(request, response):
    response.text = "Hello from the about page"
