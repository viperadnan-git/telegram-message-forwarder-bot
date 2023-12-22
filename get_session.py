from pyrogram import Client

api_id = int(input("Enter api_id: "))
api_hash = input("Enter api_hash: ")

with Client("my_account", api_id, api_hash) as app:
    print(f"Your session string is:")
    print(app.export_session_string())