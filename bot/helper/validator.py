from jsonschema import validate

"""
[pyrogram]
api_id = 12345
api_hash = "0123456789abcdef0123456789abcdef"
bot_token = "123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ"
session_string = "1BVn1-ABCD1234efgh5678IJKLmnoPQRsTUVwxyZ"
sudo_users = [123456789, 123456789]

[[chats]]
from = "123456789"
to = "123456789"

[[chats]]
from = ["123456789", "123456789"]
to = "123456789"

[[chats]]
from = "123456789"
to = ["123456789", "123456789"]

[[chats]]
from = ["123456789", "123456789"]
to = ["123456789", "123456789"]
"""

CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "pyrogram": {
            "type": "object",
            "properties": {
                "api_id": {"type": "integer"},
                "api_hash": {"type": "string"},
                "bot_token": {"type": "string"},
                "session_string": {"type": "string"},
                "sudo_users": {"type": "array", "items": {"type": "integer"}},
            },
            "required": [
                "api_id",
                "api_hash",
            ],
            "anyOf": [
                {"required": ["bot_token"]},
                {"required": ["session_string"]},
            ],
        },
        "chats": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "from": {
                        "type": ["string", "array", "integer"],
                        "items": {"type": ["string", "integer"]},
                    },
                    "to": {
                        "type": ["string", "array", "integer"],
                        "items": {"type": ["string", "integer"]},
                    },
                    "replace": {
                        "type": "object",
                        "patternProperties": {
                            "^[a-zA-Z0-9_]+$": {"type": "string"}
                        },
                    },
                },
                "required": ["from", "to"],
            },
            "minItems": 1,
        },
    },
    "required": ["pyrogram", "chats"],
}


def validate_config(config):
    validate(config, CONFIG_SCHEMA)
