import random


def xd():
    users = []

    names = ["Marian", "Gustáv", "Linda", "Linda", "Hubert", "Karol", "Imrich", "Števo",
             "Rastislav", "Arpád", "Bohuslava"]
    passwords = ["123456", "123456789", "qwerty", "aa12345678", "martin", "heslo", "martinko",
                 "veronika", "password"]

    userAdmin = {
        "username": "Imhotep",
        "password": "Husak"
    }
    users.append(userAdmin)

    for i in range(5):
        user = {
            "username": names[random.randrange(0, len(names))],
            "password": passwords[random.randrange(0, len(passwords))]
        }

        users.append(user)

    return users
