def app(environ, start_response):
    response_body = b"Hello World"
    status = "200 OK"
    response_headers = []
    start_response(status, headers=response_headers)
    return iter([response_body])
