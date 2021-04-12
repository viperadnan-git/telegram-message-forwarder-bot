import os
from pyrogram import filters
from bot import LOG, app, advance_config, chats_data, from_chats, to_chats, remove_strings, replace_string

@app.on_message(filters.chat(from_chats) & filters.incoming)
def work(client, message):
    caption = None
    msg = None
    if remove_strings:
      for string in remove_strings:
        if message.media and not message.poll:
          caption = message.caption.html.replace(string, replace_string)
        elif message.text:
          msg = message.text.html.replace(string, replace_string)
    if advance_config:
      try:
        for chat in chats_data[message.chat.id]:
          if caption:
            message.copy(chat, caption=caption)
          elif msg:
            app.send_message(chat, msg, parse_mode="html")
          else:
            message.copy(chat)
      except Exception as e:
        LOG.error(e)
    else:
      try:
        for chat in to_chats:
          if caption:
            message.copy(chat, caption=caption)
          elif msg:
            app.send_message(chat, msg)
          else:
            message.copy(chat)
      except Exception as e:
        LOG.error(e)


app.run()