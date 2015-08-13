from handlers import main, login, logout, room, user


url_patterns = [
    (r'/', main.MainHandler),
    (r'/chat', user.UserHandler),
    (r'/login', login.LoginHandler),
    (r'/logout', logout.LogoutHandler),
]
