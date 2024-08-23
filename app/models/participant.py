from .. import db

class Participants(db.Model):
    eventid = db.Column(db.Integer, nullable=False)
    eventname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    address = db.Column(db.String, nullable=False)

class Certificate(db.Model):
    eventid = db.Column(db.Integer, nullable=False)
    eventname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    address = db.Column(db.String, nullable=False)
