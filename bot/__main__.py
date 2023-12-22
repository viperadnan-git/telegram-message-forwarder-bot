import random
import logging
from time import sleep

from pyrogram import filters

from bot import app, monitored_chats, chats_map, sudo_users
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from pyrogram import Client

logging.info("Bot Started")


@app.on_message(filters.chat(monitored_chats) & filters.incoming)
def work(_:Client, message:Message):
    caption = None
    msg = None
    chat = chats_map.get(message.chat.id)
    if chat.get("replace"):
        for old, new in chat["replace"].items():
            if message.media and not message.poll:
                caption = message.caption.markdown.replace(old, new)
            elif message.text:
                msg = message.text.markdown.replace(old, new)
    try:
        for chat in chat["to"]:
            if caption:
                message.copy(chat, caption=caption, parse_mode=ParseMode.MARKDOWN)
            elif msg:
                app.send_message(chat, msg, parse_mode=ParseMode.MARKDOWN)
            else:
                message.copy(chat)
    except Exception as e:
        logging.error(f"Error while sending message from {message.chat.id} to {chat}: {e}")


@app.on_message(filters.user(sudo_users) & filters.command(["fwd", "forward"]), group=1)
def forward(app, message):
    if len(message.command) > 1:
        chat_id = int(message.command[1])
        if chat_id:
            try:
                offset_id = 0
                limit = 0
                if len(message.command) > 2:
                    limit = int(message.command[2])
                if len(message.command) > 3:
                    offset_id = int(message.command[3])
                for msg in app.iter_history(chat_id, limit=limit, offset_id=offset_id):
                    msg.copy(message.chat.id)
                    sleep(random.randint(1, 10))
            except Exception as e:
                message.reply_text(f"```{e}```")
        else:
            reply = message.reply_text(
                "```Invalid Chat Identifier. Give me a chat id, username or message link.```"
            )
            sleep(5)
            reply.delete()
    else:
        reply = message.reply_text(
            "```Invalid Command ! Use /fwd {ChatID} {limit} {FirstMessageID}```"
        )
        sleep(20)
        reply.delete()


app.run()
