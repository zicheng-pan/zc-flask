class BaseException(Exception):

    def __init__(self, code='', message='Error'):
        self.code = code
        self.message = message

    def __str__(self):
        return self.message


class EndpointExistsError(BaseException):

    def __init__(self, message="Endpoint exists!"):
        super().__init__(str(500), message=message)


class URLExistsError(BaseException):
    def __init__(self, message="URL exists!"):
        super().__init__(str(500), message=message)
