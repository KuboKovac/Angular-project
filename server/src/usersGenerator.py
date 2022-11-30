import random


def xd():
    users = []

    names = ["Marian", "Gustáv", "Linda", "Linda", "Hubert", "Karol", "Imrich", "Števo",
             "Rastislav", "Arpád", "Bohuslava", "Miloš", "Emil", "Gejza", "Gašpar", "Blažej", "Erik", "Erika", "Lívia",
             "Vlasta", "Dorota", "Viktor", "Alexander", "Eleonóra", "Albín", "Zlatica", "Miroslav", "Benjamín",
             "Marián", "Albert", "Zoltán", "Richard", "Hugo", "Izidor", "Fedor", "Justina", "Marek", "Juraj", "Elvin",
             "Slavomír", "Lea","Jaroslav", "Florián", "Gizela", "Svetozár", "Vilma", "Norbert", "Robert", "Alojz"]

    passwords = ["123456", "123456789", "qwerty", "aa12345678", "martin", "heslo", "martinko",
                 "veronika", "password", "killer", "monika", "000000", "dominika"]

    userAdmin = {
        "id": 0,
        "username": "Imhotep",
        "password": "Husak",
        "role": "Admin"
    }
    users.append(userAdmin)

    for i in range(25):
        user = {
            "id": i+1,
            "username": names[random.randrange(0, len(names))],
            "password": passwords[random.randrange(0, len(passwords))],
            "role": "Guest"
        }

        users.append(user)

    return users
