from .base import BaseHandler

class RoomHandler(object):
    def __init__(self, name, user=None):
        self.name = name
        self.subscribers = {user} if user else set()

    def add_user(self, user):
        self.subscribers.add(user)

    def remove_user(self, user):
        self.subscribers.remove(user)
