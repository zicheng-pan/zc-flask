from authsession import AuthLogin
from session_localstorefile import session
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


class SessionView(BaseView):

    @AuthLogin.auth_session
    def dispatch_request(self, request, *args, **options):
        return super(SessionView, self).dispatch_request(request, *args, **options)


class Index(SessionView):
    def get(self, request):
        user = session.get_item(request, 'user')
        return simple_template("index.html", user=user, message="hello world")


class Login(BaseView):
    def get(self, request):
        return simple_template("login.html")

    def post(self, request):
        user = request.form['user']
        session.push(request, 'user', user)
        return 'login successfully，<a href="/">返回</a>'


class Logout(SessionView):
    def get(self, request):
        session.pop(request, 'user')
        return '登出成功, <a href="/">返回</a>'


view_map = [
    {
        'url': '/',
        'view': Index,
        'endpoint': 'index'
    },
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
    }, {
        'url': '/login',
        'view': Login,
        'endpoint': 'test'
    },
    {
        'url': '/logout',
        'view': Logout,
        'endpoint': 'logout'
    }
]

index_controller = Controller('index', view_map)
app.load_controller(index_controller)

app.run()
