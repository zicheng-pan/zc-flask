import base64
import json
import os


def get_session_id(request):
    return request.cookies.get('session_id', '')


class Session:

    def __init__(self, session_path='session'):
        self.__session_map__ = {}
        self.__storage_path__ = session_path
        if not os.path.exists(self.__storage_path__):
            os.makedirs(self.__storage_path__)

    def __new__(cls, *args, **kwargs):
        # single instance
        if not hasattr(cls, '_Session__instance'):
            cls._Session__instance = super().__new__(cls, *args, **kwargs)
        return cls._Session__instance

    def set_storage_path(self, session_path):
        self.__storage_path__ = session_path
        if not os.path.exists(self.__storage_path__):
            os.makedirs(self.__storage_path__)

    def storage(self, session_id):
        filename = os.path.join(self.__storage_path__, session_id)
        with open(filename, 'wb') as f:
            content = json.dumps(self.__session_map__.get(session_id))
            f.write(base64.encodebytes(content.encode()))

    def push(self, request, item, value):
        session_id = get_session_id(request)

        if session_id in self.__session_map__:
            self.__session_map__[session_id][item] = value

        else:
            self.__session_map__[session_id] = {item: value}

    def pop(self, request, item):

        session_id = get_session_id(request)
        current_session = self.__session_map__.get(session_id, {})
        if item in current_session:
            current_session.pop(item)

    def get(self, request):
        return self.__session_map__.get(get_session_id(request), {})

    def get_item(self, request, item):
        return self.get(request).get(item, None)

    def load_all_local_session(self):
        print(self.__storage_path__)
        session_file_list = os.listdir(self.__storage_path__)
        for session_id in session_file_list:
            path = os.path.join(self.__storage_path__, session_id)
            with open(path, 'rb') as f:
                content = f.read()
                content = base64.decodebytes(content)
                self.__session_map__[session_id] = json.loads(content.decode())


session = Session()
