import re
import tornado.escape
import tornado.web

from handlers.room import RoomHandler


def command_help(user):
    message = {'html': tornado.escape.to_basestring(user.render_string('commands/help.html'))}
    user.write_message(message)


def command_list_rooms(user):
    message = {'html': tornado.escape.to_basestring(user.render_string('commands/list_rooms.html',
                                                                       rooms=user.application.rooms))}
    user.write_message(message)


def command_add_room(user, roomname):
    message = {'html': '<div class="message">Room <b>%s</b> created</div>' % roomname}
    user.application.rooms.add(RoomHandler(roomname))
    user.write_message(message)


def command_send_to(user, roomname):
    message = {'html': '<div class="message" style="text-align: center"><b>%s</b></div>'}
    user.write_message(message)


def command_login(user, username):
    message = {'html': '<div class="message" style="text-align: center"><b>%s</b></div>'}
    user.write_message(message)


def command_join_room(user, roomname):
    message = {'html': '<div class="message" style="text-align: center"><b>%s</b></div>'}
    user.write_message(message)


def command_left_room(user, roomname):
    message = {'html': '<div class="message" style="text-align: center"><b>%s</b></div>'}
    user.write_message(message)


commands = [
    {'regex': re.compile(r'/help$'), 'desc': 'list all available commands', 'pattern': '/help',
     'handler': command_help},
    {'regex': re.compile(r'/sendto (?P<param>\w+)'), 'desc': 'declare room for sending messages to',
     'pattern': '/sendto <room name>', 'handler': command_send_to},
    {'regex': re.compile(r'/rooms$'), 'desc': 'list all existing rooms', 'pattern': '/rooms',
     'handler': command_list_rooms},
    {'regex': re.compile(r'/addroom (?P<param>\w+)'), 'desc': 'create new room', 'pattern': '/addroom <room name>',
     'handler': command_add_room},
    {'regex': re.compile(r'/login \w+'), 'desc': 'login with new username', 'pattern': '/login <username>',
     'handler': command_login},
    {'regex': re.compile(r'/join \w+'), 'desc': 'join room', 'pattern': '/join <room name>',
     'handler': command_join_room},
    {'regex': re.compile(r'/left \w+'), 'desc': 'left room', 'pattern': '/left <room name>',
     'handler': command_left_room}
]
