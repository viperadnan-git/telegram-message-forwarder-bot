import logging
import os
import sys
from os import environ
import toml

from pyrogram import Client
from .helper.validator import validate_config
from jsonschema import ValidationError
from .helper.utils import parse_chats

log_level = environ.get("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    format="[%(levelname)s]\t%(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=log_level,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

config = None
if os.path.exists("config.toml"):
    config = toml.load("config.toml")
    logging.info(f"Loaded config.toml")
elif os.environ.get("CONFIG"):
    config = toml.loads(environ["CONFIG"])
    logging.info(f"Loaded config from environment variable")
else:
    logging.error(f"File config.toml and CONFIG env variable not found. Exiting...")
    sys.exit(1)


try:
    validate_config(config)
except ValidationError as error:
    logging.error(f"Invalid config: {error.message}")
    logging.info(
        f"Please read the documentation carefully and configure the bot properly."
    )
    sys.exit(1)


logging.info(f"Initalizing bot...")

monitored_chats, chats_map = parse_chats(config["chats"])
sudo_users = config["pyrogram"].get("sudo_users", [])

logging.info(f"Monitored chats: {', '.join(str(x) for x in monitored_chats)}")
logging.info(f"Chats map: {chats_map}")
logging.info(f"Sudo users: {sudo_users}")

if config["pyrogram"].get("bot_token"):
    app = Client(
        "bot",
        api_id=config["pyrogram"]["api_id"],
        api_hash=config["pyrogram"]["api_hash"],
        bot_token=config["pyrogram"]["bot_token"],
    )
else:
    app = Client(
        "bot",
        api_id=config["pyrogram"]["api_id"],
        api_hash=config["pyrogram"]["api_hash"],
        session_string=config["pyrogram"]["session_string"],
    )