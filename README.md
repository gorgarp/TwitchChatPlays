# Twitch Plays Bot for BizHawk

## Description
This bot allows Twitch chat to control a game running in the BizHawk emulator. Users in the chat can send commands which are then translated into key presses in the emulator, enabling a collaborative gameplay experience directly from Twitch chat.

## Prerequisites
- Python 3.x
- `irc` Python library
- `keyboard` Python library
- BizHawk emulator

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gorgarp/TwitchChatPlays.git
   cd TwitchChatPlays
   ```

2. **Install necessary Python libraries:**
   ```bash
   pip install irc keyboard
   ```

3. **Configure the emulator:**
   - Ensure that the BizHawk emulator is installed and properly configured for the game you wish to play.

## Configuration

1. **Set up Twitch IRC:**
   - Create a Twitch account for the bot or use an existing one.
   - Obtain an OAuth token for the Twitch IRC. This can be done through [Twitch Chat OAuth Password Generator](https://twitchapps.com/tmi/).
   - Replace the placeholders in the script with the bot's Twitch username and the OAuth token:
     ```python
     CHANNEL_NAME = "YourTwitchChannelName"
     TOKEN = "oauth:YourOAuthToken"
     ```

2. **Configure Key Mappings:**
   - Adjust the `command_map` dictionary in the script to match the controls of your game.

## Usage

1. **Run the Bot:**
   ```bash
   python [name of your python script].py
   ```

2. **Start your game in BizHawk.**

## Note
- This script is currently tested only on the BizHawk emulator.
