import string
import random


def token_generator(size):
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(size))
