from zcflask import WEBMVC

app = WEBMVC()


# Flask code example
# app = Flask(__name__)
#
# @app.route('/', methods=['GET'])
# def index():
#     return 'Hello, World'


@app.route('/index', methods=['GET'])
def index():
    return "testing"


@app.route('/test/js')
def test_js():
    return '<script src="/static/test.js"></script>'


app.run(use_reloader=True)
