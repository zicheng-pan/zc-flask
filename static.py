from helper import parse_static_key
from werkzeug.wrappers import Response

ERROR_MAP = {
    '401': Response('<h1>401 Unknown or unsupported method.</h1>',
                    content_type='text/html; charset=UTF-8', status=401),
    '404': Response('<h1>404 Source Not Found.<h1>',
                    content_type='text/html; charset=UTF-8', status=404),
    '503': Response('<h1>503 Unknown function type.</h1>',
                    content_type='text/html; charset=UTF-8', status=503)
}

TYPE_MAP = {
    'css': 'text/css',
    'js': 'text/js',
    'png': 'image/png',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg'
}


