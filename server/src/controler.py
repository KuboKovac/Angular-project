import Util


class Controler():

    def __init__(self,):
        self.users: list = []
        self.userTokens: dict = {}

    def setUsers(self, inputUsername):
        self.users = inputUsername

    def getUsers(self):
        userNames = {}
        for index, user in enumerate(self.users):
            userNames[index] = user["username"]

        return userNames, 200

    def checkCredential(self, username: str, password: str):
        for user in self.users:
            if user["username"] == username and user["password"] == password:
                token = Util.token_generator(40)
                self.userTokens = {
                    "username": username,
                    "token": token
                }
                return token, 201
            else:
                return "Ta so si kokot", 400
