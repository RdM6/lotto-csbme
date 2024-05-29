from urllib import request

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/signup", methods=['POST'])
def signup():
    email = request.json['email']
    password = request.json['password']

    return jsonify({
        "email": email,
        "password": password,
    })


@app.route("/login", methods=['POST'])
def login():

    return jsonify({
        "success": "yes",
    })


if __name__ == "__main__":
    app.run(debug=True)
