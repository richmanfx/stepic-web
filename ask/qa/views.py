from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')

'''
def wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    # body = 'Hello, world!'
    body = environ['QUERY_STRING'].replace('&', '\n')
    start_response(status, headers)
    return [body]
'''