class Controler():

    def __init__(self,):
        self.users: list = []

    def setUsers(self, inputUsername):
        self.users = inputUsername

    def checkCredential(self, username: str, password: str):
        for user in self.users:
            if user["username"] == username and user["password"] == password:
                return "Linus", 201
            else:
                return "Ta so si kokot", 400
