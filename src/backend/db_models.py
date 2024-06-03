from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from game import GameWinningNumbers

"""
Hier wird eine Datenbank erzeugt und zur db Variable zugewiesen.
"""
db = SQLAlchemy()

"""
Hier wird ein Universally unique identifier erzeugt und als default bei den Tabellen eingesetzt.
"""
def get_uuid():
    return uuid4().hex

"""
Hier werden die Datenbank-Tabellen-Modelle, wie "users", "game_numbers" und "user_game_numbers", erstellt.
"""
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(16), primary_key=True, unique=True, default=get_uuid)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


class GameNumbers(db.Model):
    __tablename__ = "game_numbers"
    id = db.Column(db.String(16), primary_key=True, unique=True, default=get_uuid)
    winning_numbers = db.Column(db.String(120), nullable=False, default=GameWinningNumbers.create_winning_numbers())
    winning_super_number = db.Column(db.Integer, nullable=False, default=GameWinningNumbers.create_winning_super_number())


class UserGameStats(db.Model):
    __tablename__ = "user_game_stats"
    id = db.Column(db.String(16), primary_key=True, unique=True, default=get_uuid)
    email = db.Column(db.String(120), nullable=False)
    result = db.Column(db.String(120), nullable=False, default="empty")
    player_input_numbers = db.Column(db.String(120), nullable=False)
    player_input_super_number = db.Column(db.Integer, nullable=False)
