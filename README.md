# Telegram Message Forwarder Bot
A telegram bot, which can forward messages from channel, group or chat to another channel, group or chat automatically.

## Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Configuration
To configure this bot add the environment variables stated below.
- `API_ID` - Get it by creating an app on [https://my.telegram.org](https://my.telegram.org)
- `API_HASH` - Get it by creating an app on [https://my.telegram.org](https://my.telegram.org)
- `BOT_TOKEN` - Get it by creating a bot on [https://t.me/BotFather](https://t.me/BotFather)
- `FROM_CHATS` - Chat ID of the chats from where to forward messages. Seperated by space.
- `TO_CHATS` - Chat ID of the chats where to forward messages. Seperated by space.

### Installing Requirements
Install the required Python Modules in your machine. Not required if using [Heroku](https://heroku.com).
```
pip3 install -r requirements.txt
```

## Copyright & License
- Copyright (©) 2020 by [Adnan Ahmad](https://github.com/viperadnan-git)
- Licensed under the terms of the [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](./LICENSE)