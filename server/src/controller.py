import json
from cars import Car

from Util import comparison, token_generator, validateJson


class Controller:

    def __init__(self, ):
        self.users: list = []
        self.userTokens: dict = {}
        self.carObject: Car = Car()

    def setUsers(self, inputUsername):
        self.users = inputUsername

    def getUsers(self) -> tuple:
        userNames = []
        for index, user in enumerate(self.users):
            userNames.append({"id": user["id"],
                              "username": user["username"],
                              "role": user["role"]})

        return userNames, 200

    def findUserByid(self, id) -> tuple:
        for user in self.users:
            if id == user["id"]:
                return user, 200
        return {"message": "This user doesnt exist in our database"}, 400

    def checkCredential(self, username: str, password: str) -> tuple:
        for user in self.users:
            if user["username"] == username and user["password"] == password:
                token = token_generator(40)
                self.userTokens = {
                    "username": username,
                    "token": token
                }
                return {"token": token}, 201
            else:
                return "Wrong username or password", 400

    def registerUser(self, data) -> tuple:
        username = data["username"]
        password = data["password"]

        if len(username) <= 0 or len(password) <= 0:
            return {"message": "Credentials are empty or not fully filled"}, 400
        else:
            if comparison(username, self.users):
                return "User already exist", 400
            else:
                self.users.append({
                    "id": len(self.users) + 1,
                    "username": username,
                    "password": password,
                    "role": "guest"

                })
                return "User " + username + "was successfully created", 200

    def removeUser(self, id, token) -> tuple:
        for user in self.users:
            if user["id"] == id and user["role"] != "Admin":
                self.users.remove(user)
                for index, userIdReplace in enumerate(self.users):
                    userIdReplace["id"] = index
                return {"message": user["username"] + " was deleted"}, 200
        return {"Message": "Ta so"}, 400

    def updateUser(self, id, data, token) -> tuple:
        for index, user in enumerate(self.users):
            if user["id"] == id and user["role"] != "Admin":
                if validateJson(json.loads(str(data).replace("\'", "\""))):
                    data["id"] = user["id"]
                    oldUser = user
                    self.users[index] = data
                return {"Message": oldUser["username"] + " Was replaced for " + data["username"]}, 200
        return {"Message": "Ta so daco podloho tu je"}, 400

    def getCarById(self, id):
        response = self.carObject.getCarById(id)
        return response if response != [] else {"Message": "Richard"}

    def getAllCars(self) -> list:
        return self.carObject.getCarList()

    def updateCarById(self, id, data, token):
        return self.carObject.updateCar(id, data)

    def removeCarById(self, id,token) -> tuple:
        return self.carObject.RemoveCarById(id)

    def addNewCar(self, data,token):
        return self.carObject.AddNewCar(data)