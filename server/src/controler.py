import json

from Util import comparison, token_generator, validateJson


class Controler:

    def __init__(self, ):
        self.users: list = []
        self.userTokens: list = []

    def setUsers(self, inputUsername):
        self.users = inputUsername

    def getUsers(self) -> tuple:
        userNames = []
        for index, user in enumerate(self.users):
            userNames.append({"id": user["id"],
                                "username": user["username"],
                                "password": user["password"],
                                "role": user["role"]})

        return userNames, 200

    def getUserTokens(self):
        return self.userTokens

    def findUserByid(self, id) -> tuple:
        for user in self.users:
            if id == user["id"]:
                return user, 200
        return {"message": "This user doesnt exist in our database"}, 400

    def checkCredential(self, username: str, password: str) -> tuple:
        for user in self.users:
            if user["username"] == username and user["password"] == password:
                if user["username"] in self.userTokens:
                    print("taky tu už je")
                    self.userTokens.remove()
                token = token_generator(40)

                self.userTokens.append({
                    "username": username,
                    "token": token
                })
                return {"token": token}, 201
        return {"message": "Ta so si kokot"}, 400

    def registerUser(self, data) -> tuple:
        username = data["username"]
        password = data["password"]

        if len(username) <= 0 or len(password) <= 0:
            return {"message": "Credentials are empty or not fully filled"}, 400
        else:
            if comparison(username, self.users):
                return {"message": "already exist"}, 400
            else:
                self.users.append({
                    "id": len(self.users) + 1,
                    "username": username,
                    "password": password,
                    "role": "guest"

                })
                return {"message": username + " was successfully created"}, 200

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
