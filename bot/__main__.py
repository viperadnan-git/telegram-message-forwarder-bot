import os
import random
from time import sleep
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup)
from bot import LOG, app, advance_config, chats_data, from_chats, to_chats, \
    remove_strings, replace_string, sudo_users
from bot.helper.utils import get_formatted_chat

LOG.info("Welcome, this is the telegram-message-forwarder-bot. main routine...")


@app.on_message(filters.chat(from_chats) & filters.incoming & ~filters.reply & ~filters.poll)
def work(client, message):
    if advance_config:
        try:
            for chat in chats_data[message.chat.id]:
                send_message(message, chat)
        except Exception as e:
            LOG.error(e)
    else:
        try:
            for chat in to_chats:
                send_message(message, chat)
                # app.forward_messages(chat, message.chat.id, message.message_id)
        except Exception as e:
            LOG.error(e)


def send_message(message, chat):
    sender_name_parts = []
    if message.from_user.first_name:
        sender_name_parts.append(message.from_user.first_name)
    if message.from_user.last_name:
        sender_name_parts.append(message.from_user.last_name)
    if message.from_user.username:
        sender_name_parts.append("@"+message.from_user.username)
    sender_name = " ".join(sender_name_parts)
    from_chat = str(message.chat.id).replace("-100", "")
    message_link = f"https://t.me/c/{from_chat}/{message.message_id}"

    LOG.info(
        f"Send message from: {sender_name} / {message.chat.title} to chat: {chat} ")
    LOG.debug(f"Send message: {message}")

    buttons = [InlineKeyboardButton(f"{message.chat.title}", url=message_link)]
    if message.from_user.username:
        buttons.append(
            InlineKeyboardButton(f"PN {sender_name}", url=f"https://t.me/{message.from_user.username}"))
    app.copy_message(
        chat, message.chat.id, message.message_id,
        reply_markup=InlineKeyboardMarkup([buttons]))


@ app.on_message(filters.user(sudo_users) & filters.command(["fwd", "forward"]), group=1)
def forward(app, message):
    if len(message.command) > 1:
        chat_id = get_formatted_chat(message.command[1], app)
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
                "```Invalid Chat Identifier. Give me a chat id, username or message link.```")
            sleep(5)
            reply.delete()
    else:
        reply = message.reply_text(
            "```Invalid Command ! Use /fwd {ChatID} {limit} {FirstMessageID}```")
        sleep(20)
        reply.delete()


app.run()
