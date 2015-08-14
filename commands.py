import re
import tornado.escape
import tornado.web
import logging

from handlers.room import RoomHandler
from handlers.base import BaseHandler

def command_help(user):
    message = {'html': tornado.escape.to_basestring(user.render_string('commands/help.html'))}
    user.write_message(message)


def command_list_rooms(user):
    message = {'html': tornado.escape.to_basestring(user.render_string('commands/list_rooms.html',
                                                                       rooms=user.application.rooms))}
    user.write_message(message)


def command_my_list_rooms(user):
    message = {'html': tornado.escape.to_basestring(user.render_string('commands/list_rooms.html',
                                                                       rooms=user.rooms))}
    user.write_message(message)


def command_add_room(user, roomname):
    message = {'html': '<div class="message" style="text-align: center">Room <b>%s</b> created</div>' % roomname}
    user.application.rooms.add(RoomHandler(roomname))
    user.write_message(message)


def command_send_to(user, roomname):
    room = next((x for x in user.application.rooms if x.name == roomname), None)
    message = {}
    if room:
        if room in user.rooms:
            user.default_send_room = room
            message['html'] = '<div class="message" style="text-align: center">Your messages will send to <b>%s</b></div>' % roomname
        else:
            message['html'] = '<div class="message" style="text-align: center">You are no joined to <b>%s</b><br>First of all join the room!</div>' % roomname
    else:
        message['html'] = '<div class="message" style="text-align: center">There is no such room></div>'
    user.write_message(message)


# def command_login(user, username):
#     old_username = user.get_current_user().decode('utf-8')
#     tornado.web.RequestHandler.set_secure_cookie(user.current_user, 'user', username)
#     #user.set_secure_cookie('user', username)
#     for subscriber in user.default_send_room.subscribers:
#         try:
#             message = {'html': '<div class="message" style="text-align: center">User <b>%s</b> changed name to <b>%s</b></div>' % (old_username, username)}
#             subscriber.write_message(message)
#         except:
#             logging.error("Error sending message", exc_info=True)
#     message = {'html': '<div class="message" style="text-align: center"><b>%s</b></div>'}
#     user.write_message(message)


def command_join_room(user, roomname):
    room = next((x for x in user.application.rooms if x.name == roomname), None)
    message = {}
    if room:
        if user in room.subscribers:
            message['html'] = '<div class="message" style="text-align: center">You already joined to <b>%s</b></div>', roomname
        else:
            message['html'] = '<div class="message" style="text-align: center">User <b>%s</b> joined room <b>%s</b></div>' % (user.current_user.decode('utf-8'), roomname)
            for subscriber in room.subscribers:
                try:
                    subscriber.write_message(message)
                except:
                    logging.error("Error sending message", exc_info=True)
            room.subscribers.add(user)
            user.rooms.add(room)
            message['html'] = '<div class="message" style="text-align: center">You joined room <b>%s</b></div>' % roomname

    else:
        message['html'] = '<div class="message" style="text-align: center">There is no such room</div>'
    user.write_message(message)


def command_left_room(user, roomname):
    room = next((x for x in user.application.rooms if x.name == roomname), None)
    message = {}
    if room:
        if user in room.subscribers:
            message['html'] = '<div class="message" style="text-align: center">User <b>%s</b> left room <b>%s</b></div>' % (
                user.current_user.decode('utf-8'), roomname)
            room.subscribers.remove(user)
            for subscriber in room.subscribers:
                try:
                    subscriber.write_message(message)
                except:
                    logging.error("Error sending message", exc_info=True)
            user.rooms.remove(room)
            message['html'] = '<div class="message" style="text-align: center">You successfully left <b>%s</b></div>' % roomname
        else:
            message['html'] = '<div class="message" style="text-align: center">You are no joined to room <b>%s</b></div>' % roomname
    else:
        message['html'] = '<div class="message" style="text-align: center">There is no such room</div>'
    user.write_message(message)


commands = [
    {'regex': re.compile(r'/help$'), 'desc': 'list all available commands', 'pattern': '/help',
     'handler': command_help},
    {'regex': re.compile(r'/sendto (?P<param>\w+)'), 'desc': 'declare room for sending messages to',
     'pattern': '/sendto <room name>', 'handler': command_send_to},
    {'regex': re.compile(r'/rooms$'), 'desc': 'list all existing rooms', 'pattern': '/rooms',
     'handler': command_list_rooms},
    {'regex': re.compile(r'/myrooms$'), 'desc': 'list rooms that you are joined in', 'pattern': '/myrooms',
     'handler': command_my_list_rooms},
    {'regex': re.compile(r'/addroom (?P<param>\w+)'), 'desc': 'create new room', 'pattern': '/addroom <room name>',
     'handler': command_add_room},
    # {'regex': re.compile(r'/login (?P<param>\w+)'), 'desc': 'login with new username', 'pattern': '/login <username>',
    #  'handler': command_login},
    {'regex': re.compile(r'/join (?P<param>\w+)'), 'desc': 'join room', 'pattern': '/join <room name>',
     'handler': command_join_room},
    {'regex': re.compile(r'/left (?P<param>\w+)'), 'desc': 'left room', 'pattern': '/left <room name>',
     'handler': command_left_room}
]
