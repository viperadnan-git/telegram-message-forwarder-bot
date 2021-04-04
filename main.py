from os import environ
from pyrogram import Client, filters

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
bot_token = environ["BOT_TOKEN"]
tg_session = environ.get("TELEGRAM_SESSION", None)
from_chats = list(set(int(x) for x in environ.get("FROM_CHATS").split()))
to_chats = list(set(int(x) for x in environ.get("TO_CHATS").split()))

if tg_session:
  app = Client(tg_session, api_id, api_hash)
else:
  app = Client(":memory:", api_id, api_hash, bot_token=bot_token)


@app.on_message(filters.chat(from_chats) & filters.incoming)
def work(client, message):
    try:
      for chat in to_chats:
        message.copy(chat)
    except Exception as e:
      print(e)

app.run()
