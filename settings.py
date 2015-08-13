import tornado
import os
from tornado.options import define, options
import tornado.template

path = lambda root, *a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

define('port', default=8000, type=int, help='server runs on the given port')
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")
tornado.options.parse_command_line()

STATIC_ROOT = path(ROOT, 'static')
TEMPLATE_ROOT = path(ROOT, 'templates')


settings = dict(
    cookie_secret='some_secret_value',
    template_path=TEMPLATE_ROOT,
    static_path=STATIC_ROOT,
    xsrf_cookies=True,
)
