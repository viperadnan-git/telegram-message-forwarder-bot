import sys

def get_formatted_chats(chats, app):
    formatted_chats = []
    for chat in chats:
      try:
        if isInt(chat):
          formatted_chats.append(int(chat))
        elif chat.startswith("@"):
          formatted_chats.append(app.get_chat(chat.replace("@", "")).id)
        elif chat.startswith("https://t.me/c/") or chat.startswith("https://telegram.org/c/") or chat.startswith("https://telegram.dog/c/"):
          chat_id = chat.split("/")[4]
          if isInt(chat_id):
            chat_id = "-100" + chat_id
            chat_id = app.get_chat(int(chat_id)).id
          formatted_chats.append(chat_id)
      except Exception as e:
        LOG.error(e)
        sys.exit(1)
    return formatted_chats

def isInt(value):
  try:
    int(value)
    return True
  except ValueError:
    return False