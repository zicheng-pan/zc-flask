import os

from werkzeug.serving import run_simple
from werkzeug.wrappers import Response
from werkzeug.wrappers import Request
import exceptions

from ExecFunc import ExecFunc
from helper import parse_static_key
from static import ERROR_MAP, TYPE_MAP


## WSGI main process callback method
def wsgi_app(app, environ, start_response):
    request = Request(environ)
    response = app.dispatch_request(request)
    return response(environ, start_response)


class WEBMVC:

    def __init__(self, static_folder='static'):
        self.host = "127.0.0.1"
        self.port = 8080
        self.static_map = {}  # url --> static resource
        self.url_map = {}  # url ---> endpoint
        self.function_map = {}  # endpoint --> ExecFunc
        self.static_folder = static_folder
        self.function_map['static'] = ExecFunc(func=self.dispatch_static, func_type='static')

    def dispatch_request(self, request):
        status = 200
        headers = {
            'Server': 'hello webserver'
        }

        return Response('<h1>Hello, Framework</h1>', content_type='text/html',
                        headers=headers, status=status)

    def dispatch_static(self, static_path):

        if not os.path.exists(static_path):
            return ERROR_MAP['404']

        key = parse_static_key(static_path)
        file_type = TYPE_MAP.get(key, "test/plain")
        with open(static_path, 'rb') as f:
            data = f.read()
        return Response(data, content_type=file_type)

    def run(self, host=None, port=None, **options):
        for key, value in options.items():
            if value:
                setattr(self, key, value)

        if host:
            self.host = host

        if port:
            self.port = port

        run_simple(hostname=self.host, port=self.port, application=self, **options)

    def __call__(self, environ, start_response):
        return wsgi_app(self, environ, start_response)

    def add_url_role(self, url, func, func_type, endpoint=None, **options):

        if endpoint is None:
            endpoint = func.__name__

        if url in self.url_map:
            raise exceptions.URLExistsError

        if endpoint in self.function_map and func_type != 'static':
            raise exceptions.EndpointExistsError

        self.url_map[url] = endpoint

        self.function_map[endpoint] = ExecFunc(func, func_type, **options)
