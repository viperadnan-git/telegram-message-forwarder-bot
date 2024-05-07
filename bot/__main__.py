import random
import logging
from time import sleep
import traceback

from pyrogram import filters

from bot import app, monitored_chats, chats_map, sudo_users
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from pyrogram import Client

logging.info("Bot Started")


@app.on_message(filters.chat(monitored_chats) & filters.all)
def work(_:Client, message:Message):
    caption = None
    msg = message.text
    chat = chats_map.get(message.chat.id)
    if chat.get("replace"):
        for old, new in chat["replace"].items():
            if message.media and not message.poll:
                caption = message.caption.markdown.replace(old, new)
            elif message.text:
                msg = message.text.markdown.replace(old, new)
    try:
        for chat in chat["to"]:
            if caption and should_send_message(caption):
                message.copy(chat, caption=caption, parse_mode=ParseMode.MARKDOWN)
            elif msg and should_send_message(msg):
                app.send_message(chat, msg, parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        logging.error(f"Error while sending message from {message.chat.id} to {chat}: {e}")


@app.on_message(filters.user(sudo_users) & filters.command(["fwd", "forward"]), group=1)
def forward(client:Client, message:Message):
    if len(message.command) > 1 and message.command[1].isdigit():
        chat_id = int(message.command[1])
        if chat_id:
            try:
                offset_id = 0
                limit = 0
                if len(message.command) > 2:
                    limit = int(message.command[2])
                if len(message.command) > 3:
                    offset_id = int(message.command[3])
                for msg in client.get_chat_history(chat_id, limit=limit, offset_id=offset_id):
                    msg.copy(message.chat.id)
                    sleep(random.randint(1, 5))
            except Exception as e:
                message.reply_text(f"Error:\n```{traceback.format_exc()}```")
        else:
            message.reply_text(
                "Invalid Chat Identifier. Give me a chat id."
            )
    else:
        message.reply_text(
            "Invalid Command\nUse /fwd {chat_id} {limit} {first_message_id}"
        )


def should_send_message(message):
    keywords = chats_map["filter"]
    if not keywords or len(keywords) == 0:
        return True
    return any(keyword in message.lower() for keyword in keywords)

app.run()