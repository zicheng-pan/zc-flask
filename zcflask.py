from werkzeug.serving import run_simple
from werkzeug.wrappers import Response
from werkzeug.wrappers import Request



## WSGI main process callback method
def wsgi_app(app, environ, start_response):
    request = Request(environ)
    response = app.dispatch_request(request)
    return response(environ, start_response)


class WEBMVC:

    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 8080

    def dispatch_request(self,request):
        status = 200
        headers = {
            'Server': 'hello webserver'
        }

        return Response('<h1>Hello, Framework</h1>', content_type='text/html',
                        headers=headers, status=status)

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
