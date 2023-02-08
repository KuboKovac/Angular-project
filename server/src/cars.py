from init_cars import carList


class Car:

    def __init__(self):
        self.carList: list = []
        for obj in carList:
            self.carList.append(obj)

    def setCarlist(self, value) -> None:
        self.carList.append(value)

    def getCarList(self) -> list:
        return self.carList

    def getCarById(self, id) -> list:
        return [
            i for i in self.carList
            if id == i["id"]
        ]

    def RemoveCarById(self, id) -> tuple:
        if len(self.carList) < int(id):
            return {"Message": f"you entered a {id}, but there are only {len(self.carList)} cars"}, 400

        for car in self.carList:
            if car["id"] == int(id):
                self.carList.remove(car)
                return {"message": car["vehicleBrand"] + " was deleted"}, 200

        return {"Message": "This car with this id doesn't exist"}, 400

    def AddNewCar(self, data) -> tuple:
        if all(key in data for key in ["id", "vehicleModel", "vehicleBrand", "licensePlate", "imageUrl", "owner","price","kilometers"]):

            if next((i for i in self.carList if i["licensePlate"] == data["licensePlate"]), None):
                return {"Message": "Car with this license plate exist"}, 400

            self.carList.append(
                {
                    "id": len(self.carList) + 1,
                    "vehicleModel": data["vehicleModel"],
                    "vehicleBrand": data["vehicleBrand"],
                    "licensePlate": data["licensePlate"],
                    "imageUrl": data["imageUrl"],
                    "owner": data["owner"],
                    "price": data["price"],
                    "kilometers": data["kilometers"]
                }
            )

            return {"Message": "Car has been added"}, 200
        else:
            return {"Message": "Bad json format"}, 400

    def updateCar(self, id, data) -> tuple:
        for index, car in enumerate(self.carList):
            if car["id"] == id:
                if all(key in data for key in ["id", "vehicleModel", "vehicleBrand",
                                               "licensePlate", "imageUrl", "owner","price","kilometers"]):
                    data["id"] = car["id"]
                    self.carList[index] = data
                return {"Message": "Car has been updated"}, 200
        return {"Message": "Ta so daco podloho tu je"}, 400
