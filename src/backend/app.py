import sqlite3
from flask import Flask, jsonify, request, session
from flask_session import Session
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from config import ApplicationConfig
from db_models import db, User, GameNumbers, UserGameStats


app = Flask(__name__)

app.config.from_object(ApplicationConfig)
bcrypt = Bcrypt(app)
server_session = Session(app)
CORS(app, supports_credentials=True)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/signup", methods=['POST'])
def signup():
    email = request.json['email']
    password = request.json['password']

    user_exists = User.query.filter_by(email=email).first() is not None

    if user_exists:
        return jsonify({'error': 'Email already registered'}), 409

    hashed_password = bcrypt.generate_password_hash(password)
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    session["user_id"] = new_user.id
    session["user_email"] = new_user.email

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
    session["user_email"] = user.email

    return jsonify({
        "id": user.id,
        "email": user.email
    })


@app.route("/@me")
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({
            "Error": "Unauthorized"
        }), 401

    user = User.query.filter_by(id=user_id).first()
    return jsonify({
        "id": user.id,
        "email": user.email,
    })


@app.route("/logout", methods=["POST"])
def logout_user():
    session.pop("user_id")
    return "200"


@app.route("/game", methods=["POST"])
def game():
    user_id = session.get("user_id")
    user_email = session.get("user_email")

    if not user_id:
        return jsonify({
            "Error": "Unauthorized"
        }), 401

    player_input_numbers = request.json["player_input_numbers"]
    player_input_super_number = request.json["player_input_super_number"]

    # Connect to the SQLite database
    conn = sqlite3.connect('./instance/database.db')
    cursor = conn.cursor()

    # Execute the query
    cursor.execute("SELECT COUNT(*) FROM game_numbers")

    # Fetch the result
    row_count = cursor.fetchone()[0]

    # Check if the table has rows
    if row_count > 0:
        print("The table has rows.")
    else:
        print("The table is empty.")
        print("Creating a new row.")
        new_game_winning_numbers = GameNumbers()
        db.session.add(new_game_winning_numbers)
        db.session.commit()
        session["game_numbers_id"] = new_game_winning_numbers.id
        session["game_winning_numbers"] = new_game_winning_numbers.winning_numbers
        session["game_winning_super_number"] = new_game_winning_numbers.winning_super_number

    # Close the connection
    conn.close()

    game_numbers_exists = GameNumbers.query.filter_by()

    if game_numbers_exists:
        game_winning_numbers = GameNumbers.query.filter_by(winning_numbers=player_input_numbers).first()
        game_winning_super_number = GameNumbers.query.filter_by(winning_super_number=player_input_super_number).first()
        if game_winning_numbers and game_winning_super_number:
            game_result = "Jackpot"
            new_user_game_stats = UserGameStats(email=user_email,
                                                result=game_result,
                                                player_input_numbers=player_input_numbers,
                                                player_input_super_number=player_input_super_number
                                                )
            db.session.add(new_user_game_stats)
            db.session.commit()
            session["user_game_stats"] = new_user_game_stats.id
            return jsonify({
                "Result": "Jackpot"
            })
        elif game_winning_numbers:
            game_result = "Win"
            new_user_game_stats = UserGameStats(email=user_email,
                                                result=game_result,
                                                player_input_numbers=player_input_numbers,
                                                player_input_super_number=player_input_super_number
                                                )
            db.session.add(new_user_game_stats)
            db.session.commit()
            session["user_game_stats"] = new_user_game_stats.id
            return jsonify({
                "Result": "Win"
            })
        else:
            game_result = "Lost"
            new_user_game_stats = UserGameStats(email=user_email,
                                                result=game_result,
                                                player_input_numbers=player_input_numbers,
                                                player_input_super_number=player_input_super_number
                                                )
            print("new_user_game_stats:", new_user_game_stats.id)
            db.session.add(new_user_game_stats)
            db.session.commit()
            session["user_game_stats"] = new_user_game_stats.id
            return jsonify({
                "Result": "Lost"
            })


if __name__ == "__main__":
    app.run(debug=True)
