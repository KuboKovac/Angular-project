import json
from flask import Flask, jsonify, request, Response
import controler
import usersGenerator

app = Flask(__name__)
cont = controler.Controler()


@app.route('/')
def WithOutParameters() -> Response:
    return jsonify('server UP! version 1.0')


@app.route("/login", methods=["POST"])
def login() -> tuple:
    req = request.data
    req_decoded = req.decode("utf-8")
    json_req = json.loads(req_decoded)
    return cont.checkCredential(json_req["username"], json_req["password"])


@app.route("/user/all", methods=["GET"])
def getAllUser() -> tuple:
    return cont.getUsers()


@app.route("/user/<id>", methods=["GET"])
def getUserById(id) -> tuple:
    return cont.findUserByid(int(id))


@app.route("/user/new", methods=["POST"])
def registerUser():
    req = request.data
    req_decoded = req.decode("utf-8")
    json_req = json.loads(req_decoded)
    return cont.registerUser(json_req)

if __name__ == '__main__':
    users: tuple = usersGenerator.xd()
    print(users)
    cont.setUsers(users)
    app.run(debug=True, port=6969)
