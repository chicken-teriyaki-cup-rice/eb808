<p align="center">
<img src="https://user-images.githubusercontent.com/91502105/212605309-5b8c4af8-4767-4aac-a8f0-5ee98791e58b.png?raw=True">
</p>
---

# eb808

eb808 is a simple and user-friendly Python web framework designed for educational purposes. Built on the WSGI standard, it seamlessly integrates with popular application servers such as Gunicorn, making it easy to deploy and scale your web applications. I created this framework to teach myself how web frameworks work. However, my ultimate goal is to use this framework as a foundation for a unique and valuable resource: an API dedicated to the study and preservation of native Hawaiian ethnobotany. This API will provide access to a vast collection of information on the traditional uses of native Hawaiian plants, promoting a deeper understanding and appreciation of the rich cultural heritage of Hawaii. This framework serves as the resilient and flexible foundation for the native Hawaiian ethnobotany platform.

## Quick Start

Install it:

```bash
pip install eb808
```

Basic Usage:

```python
# app.py
from eb808.api import API

app = API()


@app.route("/")
def home(req, resp):
    resp.text = "Hello, this is a home page."


@app.route("/about")
def about_page(req, resp):
    resp.text = "Hello, this is an about page."

@app.route("/json")
def json_handler(req, resp):
    resp.json = {"this": "is JSON"}


@app.route("/custom")
def custom_response(req, resp):
    resp.body = b'any other body'
    resp.content_type = "text/plain"
```

Start:

```bash
gunicorn app:app
```

## Features

- WSGI compatible
- Parameterized and basic routing
- Class based handlers
- Test Client
- Support for templates
- Support for static files
- Custom exception handler
- Middleware

## TODO
- Add ORM
