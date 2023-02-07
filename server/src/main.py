import json
from flask import Flask, jsonify, request, Response
from flask_cors import CORS

import controler
import usersGenerator

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})
cont = controler.Controler()


@app.errorhandler(400)
def handle_bad_request(e):
    return jsonify({"Message": 'bad request asi !'}, 400)


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"Message": "Ty gadžo taka stránka neexistuje"}), 404


@app.errorhandler(405)
def request_not_allowed(e):
    return jsonify({"Message": "Ty gadžo tadiaľ neprejdeš"}), 405


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


@app.route("/user/delete/<id>", methods=["DELETE"])
def removeUser(id):
    token = request.headers.get("Authorization")
    return cont.removeUser(int(id), token)


@app.route("/user/update/<id>", methods=["PUT"])
def updateUser(id):
    token = request.headers.get("Authorization")
    req = request.data
    req_decoded = req.decode("utf-8")
    json_req = json.loads(req_decoded)
    return cont.updateUser(int(id), json_req, token)


@app.route("/car/<id>", methods=["GET"])
def getCar(id):
    req = request.data
    return cont.getCarById(int(id))


@app.route("/car/all", methods=["GET"])
def GetAllCars():
    return cont.getAllCars()


if __name__ == '__main__':
    users: tuple = usersGenerator.xd()
    cont.setUsers(users)
    app.run(debug=True, port=6969)
