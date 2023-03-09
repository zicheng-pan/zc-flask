class Route:

    def __init__(self, app):
        self.app = app

    def __call__(self, url, **options):
        if 'methods' not in options:
            options['methods'] = ['GET','POST']

        def decorator(f):
            self.app.add_url_role(url, f, 'route', **options)
            return f

        return decorator
