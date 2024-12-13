from utils.db import db

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    release_year = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    cast = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)


class Buynow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    card_number = db.Column(db.String(1000), nullable=False)
    expiry_date = db.Column(db.String(100), nullable=False)
    cvv = db.Column(db.String(100), nullable=False)

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(1000), nullable=False)

class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(1000), nullable=False)


