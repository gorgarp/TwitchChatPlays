import irc.client
import keyboard
import time

CHANNEL_NAME = "ChannelName"
TOKEN = "oauth:xxxxxxxxxxxxx"

command_map = {
    'a': '4',
    'b': '3',
    'start': 'enter',
    'select': 'backspace',
    'up': 'w',
    'down': 's',
    'left': 'a',
    'right': 'd',
    'L': '1',
    'r': '2',
    'x': '5',
    'y': '9',
}

def on_connect(connection, event):
    connection.join('#' + CHANNEL_NAME)
    
def on_pubmsg(connection, event):
    message = event.arguments[0].lower().split()
    directional_commands = {'left': 'a', 'right': 'd', 'up': 'w', 'down': 's'}

    if len(message) == 2 and message[0] in directional_commands and message[1].isdigit():
        num_presses = int(message[1])
        if num_presses % 5 == 0 and num_presses <= 25:
            for _ in range(num_presses):
                keyboard.press(directional_commands[message[0]])  
                time.sleep(0.1)  
                keyboard.release(directional_commands[message[0]])  
            print(f"Pressed {directional_commands[message[0]]} {num_presses} times for command '{message[0]}'")
    elif message[0] in command_map:
        keyboard.press(command_map[message[0]])  
        time.sleep(0.1)  
        keyboard.release(command_map[message[0]])  
        print(f"Pressed and released {command_map[message[0]]} for command '{message[0]}'")

irc_client = irc.client.Reactor()
connection = irc_client.server().connect("irc.chat.twitch.tv", 6667, CHANNEL_NAME, password=TOKEN)
connection.add_global_handler("welcome", on_connect)
connection.add_global_handler("pubmsg", on_pubmsg)

irc_client.process_forever()
