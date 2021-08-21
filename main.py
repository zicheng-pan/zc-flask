from zcflask import WEBMVC
from view import BaseView, Controller
from zcflask import simple_template

app = WEBMVC()


# Flask code example
# app = Flask(__name__)
#
# @app.route('/', methods=['GET'])
# def index():
#     return 'Hello, World'


# @app.route('/index', methods=['GET'])
# def index():
#     return "testing"
#
#
# @app.route('/test/js')
# def test_js():
#     return '<script src="/static/test.js"></script>'


class GetView(BaseView):
    def get(self, request):
        return 'get view'


class PostView(GetView):
    def post(self, request):
        return "post view"


class RenderTemplate(BaseView):
    def get(self, request):
        return simple_template("index.html", user="testUser", message="hello world")


view_map = [
    {
        'url': '/index/view/get',
        'view': GetView,
        'endpoint': 'getindex'
    },
    {
        'url': '/index/view/post',
        'view': PostView,
        'endpoint': 'postindex'
    },
    {
        'url': '/index/rendertemplate',
        'view': RenderTemplate,
        'endpoint': 'rendertemplate'
    }
]

index_controller = Controller('index', view_map)
app.load_controller(index_controller)

app.run(use_reloader=True)
