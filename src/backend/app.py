from flask import Flask, jsonify, request, session
from flask_bcrypt import Bcrypt
from db_models import db, User

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

bcrypt = Bcrypt(app)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/signup", methods=['POST'])
def signup():
    email = request.json['email']
    password = request.json['password']
    print("Request json:", request.json)

    print("Request json names:", request.json["first_name"], request.json["last_name"])
    if hasattr(request.json, "first_name") and hasattr(request.json, "last_name"):
        first_name = request.json["first_name"]
        last_name = request.json["last_name"]
    else:
        first_name = None
        last_name = None

    user_exists = User.query.filter_by(email=email).first() is not None

    if user_exists:
        return jsonify({'error': 'Email already registered'}), 409
    else:
        hashed_password = bcrypt.generate_password_hash(password)
        new_user = User(email=email, password=hashed_password, first_name=first_name, last_name=last_name)
        db.session.add(new_user)
        db.session.commit()
        session["user_id"] = new_user.id

    return jsonify({
        "id": new_user.id,
        "email": new_user.email,
    })


@app.route("/login", methods=['POST'])
def login():
    email = request.json["email"]
    password = request.json["password"]

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"Error": "Unauthorized access."}), 401

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"Error": "Unauthorized."}), 401

    session["user_id"] = user.id

    return jsonify({
        "id": user.id,
        "email": user.email
    })


if __name__ == "__main__":
    app.run(debug=True)
