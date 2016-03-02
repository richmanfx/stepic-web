# WSGI application for Stepic.org


def wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    # body = 'Hello, world!'
    body = environ['QUERY_STRING'].replace('&', '\n')
    start_response(status, headers)
    return [body]
