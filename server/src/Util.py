import string
import random


def token_generator(size: int) -> str:
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(size))


def comparison(username: str, users: list) -> bool:
    for user in users:
        if user["username"] == username:
            return True
    return False
