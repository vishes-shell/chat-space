from .base import BaseHandler


class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        self.set_secure_cookie('user', self.get_argument('name'))
        self.redirect('/')
