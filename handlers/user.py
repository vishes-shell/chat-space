import tornado.websocket
import tornado.escape
import logging
import uuid

from .base import BaseHandler


class UserHandler(BaseHandler, tornado.websocket.WebSocketHandler):
    rooms = set()
    cache = []
    cache_size = 200
    default_send_room = None

    def open(self):
        logging.info('open')
        self.default_send_room = self.application.initial_room
        for subscriber in self.default_send_room.subscribers:
            try:
                message = {'html': '<div class="message" style="text-align: center"><b>%s</b> joined conversation</div>' % self.get_current_user().decode('utf-8')}
                subscriber.write_message(message)
                logging.info('%s', message['html'])
            except:
                logging.error("Error sending message", exc_info=True)
        self.application.initial_room.subscribers.add(self)
        self.rooms.add(self.application.initial_room)

    def on_close(self):
        if self.rooms:
            for room in self.rooms:
                room.remove_user(self)

    def connect_room(self, new_room):
        self.rooms.add(new_room)

    def send_updates(self, message):
        for subscriber in self.default_send_room.subscribers:
            try:
                message_template = 'self_message.html' if self == subscriber else 'message.html'
                message['html'] = tornado.escape.to_basestring(
                    self.render_string(message_template, message=message))
                logging.info('%s', message['html'])
                subscriber.write_message(message)
            except:
                logging.error("Error sending message", exc_info=True)

    def on_message(self, message):
        parsed = tornado.escape.json_decode(message)
        data = {
            "id": str(uuid.uuid4()),
            "body": parsed["body"],
            "user": self.get_current_user().decode('utf-8'),
            "room": self.default_send_room.name
        }
        self.send_updates(data)
