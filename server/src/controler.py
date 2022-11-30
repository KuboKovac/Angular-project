from Util import comparison, token_generator


class Controler:

    def __init__(self, ):
        self.users: list = []
        self.userTokens: dict = {}

    def setUsers(self, inputUsername):
        self.users = inputUsername

    def getUsers(self) -> tuple:
        userNames = {}
        for index, user in enumerate(self.users):
            userNames[index] = user["username"]

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
                return token, 201
            else:
                return {"message": "Ta so si kokot"}, 400

    def registerUser(self, data) -> tuple:
        username = data["username"]
        password = data["password"]

        if len(username) <= 0 or len(password) <= 0:
            return {"message": "Credentials are empty or not fully filled"}, 400
        else:
            if comparison(username, self.users) == False:
                return {"message": "already exist"}, 400
            else:
                self.users.append({
                    "id": len(self.users) + 1,
                    "username": username,
                    "password": password,
                    "role": "guest"

                })
                return {"message": username + " was successfully created"}, 200
