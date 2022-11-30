import string
import random
import jsonschema
from jsonschema import validate


def token_generator(size: int) -> str:
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(size))


def comparison(username: str, users: list) -> bool:
    for user in users:
        if user["username"] == username:
            return True
    return False


def validateJson(jsonData: dict) -> bool:
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "username": {"type": "string"},
            "password": {"type": "string"},
            "role": {"type": "string"},
        },
    }
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True
