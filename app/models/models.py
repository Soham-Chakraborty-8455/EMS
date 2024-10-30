# app/models/models.py

from .. import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        """Hashes the password and stores it."""
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        """Verifies the hashed password."""
        return check_password_hash(self.password_hash, password)

# Register the user loader callback with Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class EventDetails(db.Model):
    __tablename__ = 'event_details'
    
    id = db.Column(db.Integer, primary_key=True)
    eventname = db.Column(db.String(255), nullable=False)
    orgname = db.Column(db.String(255), unique=True, nullable=False)
    orgweb = db.Column(db.String(255))
    venue = db.Column(db.String(255), nullable=False)
    startdate = db.Column(db.String(50), nullable=False)
    enddate = db.Column(db.String(50), nullable=False)
    starttime = db.Column(db.String(50), nullable=False)
    endtime = db.Column(db.String(50), nullable=False)
    logo = db.Column(db.String(255))
    signature = db.Column(db.String(255), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    ticketTemplate = db.Column(db.String(255), nullable=False)
    certificateTemplate = db.Column(db.String(255), nullable=False)
    bannerTemplate = db.Column(db.String(255), nullable=False)
    
    # Relationships
    participants = db.relationship('Participants', backref='event', lazy=True)
    certificates = db.relationship('Certificate', backref='event', lazy=True)

class Participants(db.Model):
    __tablename__ = 'participants'
    
    id = db.Column(db.Integer, primary_key=True)
    eventid = db.Column(db.Integer, db.ForeignKey('event_details.id'), nullable=False)
    eventname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    
    # Ensure that a participant can register only once per event
    __table_args__ = (db.UniqueConstraint('eventid', 'email', name='_event_email_uc'),)

class Certificate(db.Model):
    __tablename__ = 'certificates'
    
    id = db.Column(db.Integer, primary_key=True)
    eventid = db.Column(db.Integer, db.ForeignKey('event_details.id'), nullable=False)
    eventname = db.Column(db.String(255), nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    certificateTemplate = db.Column(db.String(255), nullable=False)
    
    # Relationship
    participant = db.relationship('Participants', backref='certificate', uselist=False)
