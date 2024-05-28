
# Twitch Plays Bot for BizHawk

## Description

This bot allows Twitch chat to control a game running in the BizHawk emulator. Users in the chat can send commands which are then translated into key presses in the emulator, enabling a collaborative gameplay experience directly from Twitch chat.

## Prerequisites

- Python 3.x
- irc Python library
- keyboard Python library
- BizHawk emulator

## Installation

Clone the repository:

```sh
git clone https://github.com/gorgarp/TwitchChatPlays.git
cd TwitchChatPlays
```

Install necessary Python libraries:

```sh
pip install irc keyboard
```

### Configure the emulator

Ensure that the BizHawk emulator is installed and properly configured for the game you wish to play.

## Configuration

### Set up Twitch IRC

1. Create a Twitch account for the bot or use an existing one. (You can just use your regular account if you wish)
2. Obtain an OAuth token for the Twitch IRC. This can be done through [Twitch Chat OAuth Password Generator](https://twitchapps.com/tmi/).
3. Replace the placeholders in the script with the bot's Twitch username and the OAuth token:

```python
CHANNEL_NAME = "YourTwitchChannelName"
TOKEN = "oauth:YourOAuthToken"
```

### Configure Key Mappings

Adjust the `command_map` dictionary in the script to match the controls of your game.

### New Feature

A function has been added to allow the bot to ignore a specified character and all preceding text in chat messages. This is useful for relayed messages that include usernames.

## Usage

Run the Bot:

```sh
python main.py
```

Start your game in BizHawk.

## Note

This script is currently tested only on the BizHawk emulator.

