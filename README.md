# chat-space
Chat-space is simple tornado server which runs chat. Chat is represented by a simple interface with inbox messages,
rooms, and commands.

## Dependencies
Dependencies in `requirements.txt`. Simply run `pip install -r requirements.txt`

##Description
For supporting chat WebSocket was chose. To view the chat in work run `python app.py`
All the configuration stores in `settings.py` file and server uses `8000` port.

### ChatCommands
Chat supports several command, there is the list
```
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
    {'regex': re.compile(r'/join (?P<param>\w+)'), 'desc': 'join room', 'pattern': '/join <room name>',
     'handler': command_join_room},
    {'regex': re.compile(r'/left (?P<param>\w+)'), 'desc': 'left room', 'pattern': '/left <room name>',
     'handler': command_left_room}
]
```
Definition of handlers stored in `commands.py`
Each message checked if it belong to one of the regular expressions, if so, handler starts to work.

### Messages
Each message from users have information about creator(username) and room, from which message was sent.
For better appearance self messages putted to right side of inbox space and also don't have any info.