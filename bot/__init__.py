import os
import sys
import logging
from os import environ
from dotenv import load_dotenv
from pyrogram import Client
from bot.helper.utils import get_formatted_chats

logging.basicConfig(format='[%(asctime)s - %(pathname)s - %(levelname)s] %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOG = logging.getLogger(__name__)

if os.path.exists('config.env'):
  load_dotenv('config.env')

chats_data = {}

try:
  api_id = int(environ["API_ID"])
  api_hash = environ["API_HASH"]
  bot_token = environ.get("BOT_TOKEN", None)
  tg_session = environ.get("TELEGRAM_SESSION", None)
  sudo_users = list(set(x for x in environ.get("SUDO_USERS", "999197022").split(";")))
  try:
    from_chats = list(set(int(x) for x in environ.get("FROM_CHATS").split()))
    to_chats = list(set(int(x) for x in environ.get("TO_CHATS").split()))
  except Exception as e:
    from_chats = []
    to_chats = []
  advance_config = environ.get("ADVANCE_CONFIG", None)
  if advance_config:
    from_chats = []
  replace_string = environ.get("REPLACE_STRING", "")
except KeyError as e:
  LOG.error(e)
  LOG.error("One or more variables missing. Exiting...")
  sys.exit(1)
except ValueError as e:
  LOG.error(e)
  LOG.error("One or more variables are wrong. Exiting...")
  sys.exit(1)

try:
  remove_strings = list(set(x for x in environ.get("REMOVE_STRINGS").split(";")))
except:
  remove_strings = None

if tg_session:
  app = Client(tg_session, api_id, api_hash)
elif bot_token:
  app = Client(":memory:", api_id, api_hash, bot_token=bot_token)
else:
  LOG.error("Set either TELEGRAM_SESSION or BOT_TOKEN variable.")
  sys.exit(1)

with app:
  sudo_users = get_formatted_chats(sudo_users, app)
  LOG.info(f"Sudo users - {sudo_users}")
  if advance_config:
    for chats in advance_config.split(";"):
      chat = chats.strip().split()
      chat = get_formatted_chats(chat, app)
      f = chat[0]
      del chat[0]
      if f in chats_data:
        c = chats_data[f]
        c.extend(chat)
        chats_data[f] = c
      else:
        chats_data[f] = chat
      if not f in from_chats:
        from_chats.append(f)
    LOG.info(from_chats)
    LOG.info(chats_data)
  else:
    if len(to_chats) == 0 or len(from_chats) == 0:
      LOG.error("Set either ADVANCE_CONFIG or FROM_CHATS and TO_CHATS")
      sys.exit(1)
    else:
      from_chats = get_formatted_chats(from_chats, app)
      to_chats = get_formatted_chats(to_chats, app)
      LOG.info(from_chats)
      LOG.info(to_chats)