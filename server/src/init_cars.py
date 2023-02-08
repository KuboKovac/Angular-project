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
    "imageUrl": "https://cdn.nettivaraosa.com/live/2729897/mitsubishi-colt-00af09f0135170ce-large.jpg",
    "owner": "Richard Mižžie",
    "price": random.randrange(999, 5_500),
    "kilometers": random.randrange(450_000, 1_000_025)
},
{
    "id": 2,
    "vehicleModel": "F-150",
    "vehicleBrand": "FORD",
    "licensePlate": "VT556AP",
    "imageUrl": "https://www.rvtravel.com/wp-content/uploads/2020/08/fordcrash-696x522.jpg",
    "owner": names[random.randrange(0, len(names))],
    "price": random.randrange(999, 5_500),
    "kilometers": random.randrange(450_000, 1_000_025)
},
{
    "id": 3,
    "vehicleModel": "Mark II",
    "vehicleBrand": "TOYOTA",
    "licensePlate": "MIBOSS1",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/f/ff/1998-2000_Toyota_Mark_II.jpg",
    "owner": names[random.randrange(0, len(names))],
    "price": random.randrange(999, 5_500),
    "kilometers": random.randrange(450_000, 1_000_025)
},
{
    "id": 4,
    "vehicleModel": "CIVIC ek9(Trhač asfaltu)",
    "vehicleBrand": "HONDA",
    "licensePlate": "HE557as",
    "imageUrl": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/00-1988-honda-civic-wagovan-in-colorado-junkyard-photo-by-murilee-martin-1657766923.jpg",
    "owner": names[random.randrange(0, len(names))],
    "price": random.randrange(999, 5_500),
    "kilometers": random.randrange(450_000, 1_000_025)
},
{
    "id": 5,
    "vehicleModel": "e36 (Sidliskový sen)",
    "vehicleBrand": "BMW",
    "licensePlate": "MT831AX",
    "imageUrl": "https://i.pinimg.com/736x/c7/c2/6a/c7c26af5b86535d0ee0d12f5f90f5717.jpg",
    "owner": names[random.randrange(0, len(names))],
    "price": random.randrange(999, 5_500),
    "kilometers": random.randrange(450_000, 1_000_025)
},
{
    "id": 6,
    "vehicleModel": "ŽTR32",
    "vehicleBrand": "NISSAN",
    "licensePlate": "MISEN55",
    "imageUrl": "https://i.pinimg.com/originals/9c/36/d1/9c36d1f112a38914695b86722551b40d.jpg",
    "owner": names[random.randrange(0, len(names))],
    "price": random.randrange(999, 5_500),
    "kilometers": random.randrange(450_000, 1_000_025)
},
{
    "id": 7,
    "vehicleModel": "GOLF MK4 (Euro 6)",
    "vehicleBrand": "Volkswagen",
    "licensePlate": "KE885VT",
    "imageUrl": "https://i.imgflip.com/t037d.gif",
    "owner": "Maťko džuris",
    "price": random.randrange(999, 5_500),
    "kilometers": random.randrange(450_000, 1_000_025)
}
]