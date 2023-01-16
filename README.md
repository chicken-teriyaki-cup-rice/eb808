<p align="center">
<img src="https://user-images.githubusercontent.com/91502105/212608083-3fcced54-7407-47ea-adc3-0178aaaf886a.jpg?raw=True">
</p>
---
https://badgen.net/badge/version/0.0.3/blue
https://badgen.net/badge/build/passing/green

# eb808

I made eb808 as a simple and user-friendly Python web framework for learning purposes.

It's built on the WSGI standard, so it's easy to use with popular servers like Gunicorn. I built it mainly to teach myself web frameworks but my ultimate goal is to use it as a foundation for an API that helps with the study and preservation of native Hawaiian ethnobotany.

This API will provide access to a lot of information on traditional uses of plants in Hawaii and help with understanding and appreciating the cultural heritage of Hawaii.

## Quick Start

Install it:

```bash
pip install eb808==0.0.3
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
