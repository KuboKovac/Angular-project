import random

names = ["Marian", "Gustáv", "Linda", "Linda", "Hubert", "Karol", "Imrich", "Števo",
             "Rastislav", "Arpád", "Bohuslava", "Miloš", "Emil", "Gejza", "Gašpar", "Blažej", "Erik", "Erika", "Lívia",
             "Vlasta", "Dorota", "Viktor", "Alexander", "Eleonóra", "Albín", "Zlatica", "Miroslav", "Benjamín",
             "Marián", "Albert", "Zoltán", "Richard", "Hugo", "Izidor", "Fedor", "Justina", "Marek", "Juraj", "Elvin",
             "Slavomír", "Lea", "Jaroslav", "Florián", "Gizela", "Svetozár", "Vilma", "Norbert", "Robert", "Alojz"]

carList: list = [
{
    "id": 1,
    "vehicleModel": "KOLT",
    "vehicleBrand": "MITSUBIŠI",
    "licensePlate": "SOKERES",
    "imageUrl": "https://d2cdo4blch85n8.cloudfront.net/wp-content/uploads/2017/11/1969-%E2%80%9DDickmobile%E2%80%9D-Art-Car-by-Steve-Paige-Featured-image-672x372.jpg",
    "owner": "Richard"
},
{
    "id": 2,
    "vehicleModel": "F-150",
    "vehicleBrand": "FORD",
    "licensePlate": "FODR15",
    "imageUrl": "https://d2cdo4blch85n8.cloudfront.net/wp-content/uploads/2017/11/1969-%E2%80%9DDickmobile%E2%80%9D-Art-Car-by-Steve-Paige-Featured-image-672x372.jpg",
    "owner": names[random.randrange(0, len(names))]
},
{
    "id": 3,
    "vehicleModel": "Mark II",
    "vehicleBrand": "TOYOTA",
    "licensePlate": "TYOTA23",
    "imageUrl": "https://d2cdo4blch85n8.cloudfront.net/wp-content/uploads/2017/11/1969-%E2%80%9DDickmobile%E2%80%9D-Art-Car-by-Steve-Paige-Featured-image-672x372.jpg",
    "owner": names[random.randrange(0, len(names))]
},
{
    "id": 4,
    "vehicleModel": "CIVIC ek9(Trhač asfaltu)",
    "vehicleBrand": "HONDA",
    "licensePlate": "HNDA67",
    "imageUrl": "https://d2cdo4blch85n8.cloudfront.net/wp-content/uploads/2017/11/1969-%E2%80%9DDickmobile%E2%80%9D-Art-Car-by-Steve-Paige-Featured-image-672x372.jpg",
    "owner": names[random.randrange(0, len(names))]
},
{
    "id": 5,
    "vehicleModel": "e36 (Sidliskový sen)",
    "vehicleBrand": "BMW",
    "licensePlate": "BMW12",
    "imageUrl": "https://d2cdo4blch85n8.cloudfront.net/wp-content/uploads/2017/11/1969-%E2%80%9DDickmobile%E2%80%9D-Art-Car-by-Steve-Paige-Featured-image-672x372.jpg",
    "owner": names[random.randrange(0, len(names))]
},
{
    "id": 6,
    "vehicleModel": "ŽTR32",
    "vehicleBrand": "NISSAN",
    "licensePlate": "NIS56",
    "imageUrl": "https://d2cdo4blch85n8.cloudfront.net/wp-content/uploads/2017/11/1969-%E2%80%9DDickmobile%E2%80%9D-Art-Car-by-Steve-Paige-Featured-image-672x372.jpg",
    "owner": names[random.randrange(0, len(names))]
}
]