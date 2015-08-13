import tornado.escape

from .base import BaseHandler
from .user import UserHandler

class MainHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect('/login')
            return
        self.render("index.html", messages=UserHandler.cache)
