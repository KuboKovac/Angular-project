class Car:
    """"
    {
    id: number,
    vehicleModel: string,
    vehicleBrand: string,
    licensePlate: string,
    imageUrl: string
    owner: User
    },
    """

    def __init__(self):
        self.carList: list = []
        self.carList.append(
            {
                "id": 1,
                "vehicleModel": "MITSUBIŠI",
                "vehicleBrand": "KOLT(KOKOC)",
                "licensePlate": "SOKERES",
                "imageUrl": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DUPvL8IaRNtE&psig=AOvVaw3W2Unxq54GXU-IGL7yAegN&ust=1675870693955000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCLCc9fzeg_0CFQAAAAAdAAAAABAE",
                "owner": "Richard"
            }
        )


    def setCarlist(self, value):
        self.carList.append(value)

    def getCarList(self):
        return self.carList

    def getCarById(self, id):
        return [
            i for i in self.carList
            if id == i["id"]
        ]