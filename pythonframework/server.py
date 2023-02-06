from wsgiref.simple_server import make_server

from pythonframework.app import application

httpd = make_server (
    'localhost',
    8051,
    application
)

httpd.handle_request()
