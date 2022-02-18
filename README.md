# Telegram Message Forwarder Bot
A telegram bot, which can forward messages from channel, group or chat to another channel, group or chat automatically.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/viperadnan-git/telegram-message-forwarder-bot/)

### Configuration
To configure this bot add the environment variables stated below. Or add them in [config.env.template](./config.env.template) and change the name to `config.env`.
- `API_ID` - Get it by creating an app on [https://my.telegram.org](https://my.telegram.org)
- `API_HASH` - Get it by creating an app on [https://my.telegram.org](https://my.telegram.org)
- `BOT_TOKEN` - Get it by creating a bot on [https://t.me/BotFather](https://t.me/BotFather)
- `FROM_CHATS` - Chat ID of the chats from where to forward messages. Separated by space.
- `TO_CHATS` - Chat ID of the chats where to forward messages. Separated by space.
- `TELEGRAM_SESSION` - (Optional) If you want to use this bot as user add the telegram session name in environment variables. Get it by running [GenString](https://replit.com/@viperadnan/genstring) and select the option 1 and follow the instructions.
- `SUDO_USERS` - (Optional) Chat identifier of the sudo user. For multiple users use `;` as separator.
- `ADVANCE_CONFIG` - (Optional) If you want forward message from chat A to chat B and from chat C to chat D add this value in the format given below.
```
CHAT_ID_A CHAT_ID_B; CHAT_ID_C CHAT_ID_D
```
Or if you want to forward message from chat A to chat B, C and D. And from Chat E to Chat F
```
CHAT_ID_A CHAT_ID_B CHAT_ID_C CHAT_ID_D; CHAT_ID_E CHAT_ID_F
     ↑       ^---------------------^         ↑         ↑ to another chat
From channel       To channel        from another channel
```
- `REMOVE_STRINGS` - (Optional) Keywords to remove from message before forwarding. For multiple string use `;` as a seperator. For example -
```
@username;https://t.me/username;Hey! My channel is XXxxXX
```
- `REPLACE_STRING` - (Optional) Keyword to add in the place of `REMOVE_STRING`

### Note
- Supported identifier for a chat should be the chat id, username or message link.
- Use `/forward` command to forward older messages. For message older than 2 days you have to login as a user and set the `TELEGRAM_SESSION` variable. Command usage - `/forward <Chat ID/Username/Message Link> <Limit, No. of Messages to forward> <ID of the last message of from chat to avoid repetition>`

### Installing Requirements
Install the required Python Modules in your machine.
```
pip3 install -r requirements.txt
```
### Deployment
With python3.7 or later.
```
python3 -m bot
```

### Copyright & License
- Copyright &copy; 2021 &mdash; [Adnan Ahmad](https://github.com/viperadnan-git)
- Licensed under the terms of the [GNU General Public License Version 3 &dash; 29 June 2007](./LICENSE)
