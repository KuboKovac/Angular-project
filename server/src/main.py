import json
from flask import Flask, jsonify, request
import controler
import usersGenerator

app = Flask(__name__)
cont = controler.Controler()


@app.route('/')
def WithOutParameters():
    return jsonify('server UP! version 1.0')


@app.route("/login", methods=["POST"])
def login():
    req = request.data
    req_decoded = req.decode("utf-8")
    json_req = json.loads(req_decoded)
    return cont.checkCredential(json_req["username"], json_req["password"])


if __name__ == '__main__':
    users: tuple = usersGenerator.xd()
    print(users)
    cont.setUsers(users)
    app.run(debug=True, port=6969)
