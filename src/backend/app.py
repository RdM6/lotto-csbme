import sqlite3
from flask import Flask, jsonify, request, session
from flask_session import Session
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from config import ApplicationConfig
from db_models import db, User, GameNumbers, UserGameStats

"""
Hier wird die App erstellt mit der Hilfe von Flask.
"""
app = Flask(__name__)
"""
Hier werden die benötigten Configs von der config.py mitgegeben.
"""
app.config.from_object(ApplicationConfig)
"""
Bcrypt ermöglicht es die Passwörter von Nutzern mit den gespeicherten Hash-Werten in der Datenbank zu vergleichen,
um zu kontrollieren, ob der eingegebene Passwort sich mit dem Hash-Wert übereinstimmt.
"""
bcrypt = Bcrypt(app)
"""
Es ermöglicht mit Hilfe von Redis und der Flask-Session eine Server-sided-Session zu erzeugen.
"""
server_session = Session(app)
"""
Ist für die CORS-Fehlerbehebung da.
"""
CORS(app, supports_credentials=True)
"""
Hier wird die Datenbank initial erzeugt, bei dem App-Start.
"""
db.init_app(app)

with app.app_context():
    db.create_all()

"""
Hier wird ein /signup Route mit den POST-Methods erzeugt. 
Hier wird ein User registriert und die Daten werden in der Datenbank gespeichert.
"""
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


"""
Hier wird ein /login Route mit den POST-Methods erzeugt. 
Hier wird ein User eingeloggt und die Daten werden mit der Datenbank validiert.
"""
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

"""
Hier wird ein /@me Route erzeugt. 
Damit kann man sehen, welcher User sich gerade in der Session befindet.
"""
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

"""
Hier wird ein /logout Route mit den POST-Methods erzeugt. 
Hier wird der User ausgeloggt.
"""
@app.route("/logout", methods=["POST"])
def logout_user():
    session.pop("user_id")
    return "200"

"""
Hier wird ein /game Route mit den POST-Methods erzeugt. 
Hier befindet sich das eigentliche Spiel. Die Route kriegt die eigegebenen Zahlen von dem User 
aus dem Frontend zugeschickt und validiert diese mit der Datenbank und schickt den Resultat des Spiels
an den Frontend zurück. Die Zahlen die Spieler eingegeben hat werden dann in der DB gespeichert.
"""
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
