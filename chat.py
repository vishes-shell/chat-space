import tornado.web
import os.path
from tornado.options import define

define('port', default=8000, type=int, help='server runs on the given port')

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [

        ]
        settings = dict(
            cookie_secret='some_secret_value',
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            xsrf_cookies=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
