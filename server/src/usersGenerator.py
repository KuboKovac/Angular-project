import random


def xd():
    users = []

    names = ["Marian", "Gustáv", "Linda", "Linda", "Hubert", "Karol", "Imrich", "Števo",
             "Rastislav", "Arpád", "Bohuslava"]
    passwords = ["123456", "123456789", "qwerty", "aa12345678", "martin", "heslo", "martinko",
                 "veronika", "password"]

    userAdmin = {
        "id": 0,
        "username": "Imhotep",
        "password": "Husak",
        "role": "Admin"
    }
    users.append(userAdmin)

    for i in range(5):
        user = {
            "id": i+1,
            "username": names[random.randrange(0, len(names))],
            "password": passwords[random.randrange(0, len(passwords))],
            "role": "Guest"
        }

        users.append(user)

    return users
