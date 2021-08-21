class View:
    method = []
    methods_meta = {}

    def dispatch_request(self, request, *args, **options):
        raise NotImplementedError

    @classmethod
    def get_func(cls, name):
        def func(*args, **kw):
            return cls().dispatch_request(*args, **kw)

        func.__name__ = name
        func.__doc__ = cls.__doc__
        func.__module__ = cls.__module__
        func.methods = cls.methods

        return func


class Controller:

    def __init__(self, name, url_map):
        self.name = name
        self.url_map = url_map


class BaseView(View):
    methods = ['GET', 'POST']

    def post(self, request, *args, **options):
        pass

    def get(self, request, *args, **options):
        pass

    def dispatch_request(self, request, *args, **options):
        if request.method in self.methods:
            func = getattr(self, request.method.lower())
            return func(request, *args, **options)
        return '<h1>Unknown or unsupported require method.</h1>'
