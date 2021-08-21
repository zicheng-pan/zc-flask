from zcflask import get_session_id


class Session:

    def __init__(self):
        self.__session_map__ = {}

    def __new__(cls, *args, **kwargs):
        # single instance
        if not hasattr(cls, '_Session__instance'):
            cls._Session__instance = super().__new__(cls, *args, **kwargs)
        return cls._Session__instance

    def push(self, request, item, value):
        session_id = get_session_id(request)

        if session_id in self.__session_map__:
            self.__session_map__[session_id][item] = value

        else:
            self.__session_map__[session_id] = {item: value}

    def pop(self, request, item, value=True):

        session_id = get_session_id(request)
        current_session = self.__session_map__.get(session_id, {})
        if item in current_session:
            current_session.pop(item)

    def get(self, request):
        return self.__session_map__.get(get_session_id(request), {})

    def get_item(self, request, item):
        return self.get(request).get(item, None)


session = Session()
