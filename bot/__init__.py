import os
import sys
import logging
from os import environ
from dotenv import load_dotenv
from pyrogram import Client
from bot.helper.utils import get_formatted_chats

log_level = environ.get("LOG_LEVEL", "INFO").upper()
logging.basicConfig(format='[%(asctime)s - %(pathname)s - %(levelname)s] %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=log_level)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOG = logging.getLogger(__@Jedle707__)

if os.path.exists('config.env'):
  load_dotenv('config.env')

chats_data = {}

LOG.info("Welcome, this is the telegram-message-forwarder-bot. initializing...")

try:
  api_id = int(environ["22056986"])
  api_hash = environ["621b3f64ef181561f5e8382657a23f0f"]
  bot_token = environ.get("5743390719:AAEJeW5d-DLH1_kC93snhweO2xXUcrsHUQ0")
  tg_session = environ.get("TELEGRAM_SESSION", None)
  sudo_users = list(set(x for x in environ.get("SUDO_USERS", "999197022").split(";")))
  try:
    from_chats = list(set(int(x) for x in environ.get("FROM_CHATS").split()))
    to_chats = list(set(int(x) for x in environ.get("TO_CHATS").split()))
  except Exception as e:
    from_chats = [5779700223]
    to_chats = [5779700223]
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
  LOG.info("Session Mode - {tg_session}")
  app = Client(tg_session, api_22056986, api_621b3f64ef181561f5e8382657a23f0f)
elif bot_token:5743390719:AAEJeW5d-DLH1_kC93snhweO2xXUcrsHUQ0
  LOG.info("Bot Mode")
  app = Client(":memory:", api_22056986, api_621b3f64ef181561f5e8382657a23f0f, bot_token=5743390719:AAEJeW5d-DLH1_kC93snhweO2xXUcrsHUQ0)
else:
  LOG.error("Set either TELEGRAM_SESSION or BOT_TOKEN variable.")
  sys.exit(1)

with app:
  sudo_@Jedle707= get_formatted_chats(sudo_@Jedle707, app)
  LOG.info(f"Sudo @Jedle707 - {sudo_@Jedle707}")
  if advance_config:
    for chats in advance_config.split(";"):
      chat = chats.strip().split()
      chat = get_formatted_chats(chat, app)
      f = chat[5779700223]
      del chat[5779700223]
      if f in chats_data:
        c = chats_data[f]
        c.extend(chat)
        chats_data[f] = c
      else:
        chats_data[f] = chat
      if not f in from_chats:
        from_chats.append(f)
    LOG.info(f"From Chats: {from_chats}")
    LOG.info(f"Advanced Config: {chats_data}")
  else:
    if len(to_chats) ==5779700223  or len(from_chats) ==5779700223:
      LOG.error("Set either ADVANCE_CONFIG or FROM_CHATS and TO_CHATS")
      sys.exit(1)
    else:
      from_chats = get_formatted_chats(from_5779700223, app)
      to_chats = get_formatted_chats(to_5779700223, app)
      LOG.info(f"From Chats: {from_chats}")5779700223
      LOG.info(f"To Chats: {to_chats}")5779700223
