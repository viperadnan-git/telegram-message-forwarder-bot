import os
from os import environ
from dotenv import load_dotenv
from pyrogram import Client, filters

if os.path.exists('config.env'):
  load_dotenv('config.env')

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
bot_token = environ["BOT_TOKEN"]
tg_session = environ.get("TELEGRAM_SESSION", None)
from_chats = list(set(int(x) for x in environ.get("FROM_CHATS").split()))
to_chats = list(set(int(x) for x in environ.get("TO_CHATS").split()))
advance_config = environ.get("ADVANCE_CONFIG", None)

if tg_session:
  app = Client(tg_session, api_id, api_hash)
else:
  app = Client(":memory:", api_id, api_hash, bot_token=bot_token)

if advance_config:
  print("Advance Configures detected...")
  from_chats = []
  chats_data = {}
  for chats in advance_config.split(","):
    chat = chats.strip().split()
    chats_data[int(chat[0])] = int(chat[1])
    if not int(chat[0]) in from_chats:
      from_chats.append(int(chat[0]))
  print(from_chats)
  print(chats_data)
    

@app.on_message(filters.chat(from_chats) & filters.incoming)
def work(client, message):
    if advance_config:
      try:
        message.copy(chats_data[int(message.chat.id)])
      except Exception as e:
        print(e)
    else:
      try:
        for chat in to_chats:
          message.copy(chat)
      except Exception as e:
        print(e)

app.run()
