from session_localstorefile import session


class AuthSession:

    @classmethod
    def auth_session(cls, f, *args, **options):
        def decorator(obj, request):
            if cls.auth_logic(request, *args, **options):
                return f(obj, request)
            return cls.auth_fail_callback(request, *args, **options)

        return decorator

    @staticmethod
    def auth_logic(request, *args, **options):
        raise NotImplementedError

    @staticmethod
    def auth_fail_callback(request, *args, **options):
        raise NotImplementedError


class AuthLogin(AuthSession):

    @staticmethod
    def auth_fail_callback(request, *args, **options):
        return '<a href="/login">登录</a>'

    @staticmethod
    def auth_logic(request, *args, **options):
        if 'user' in session.get(request):
            return True
        return False
