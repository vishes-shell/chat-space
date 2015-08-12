import tornado.web
import tornado.ioloop
import tornado.websocket
from tornado.options import options

from settings import settings
from urls import url_patterns


class ChatSpace(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    app = ChatSpace()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
