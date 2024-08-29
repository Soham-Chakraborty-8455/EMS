from .. import db

class EventDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eventname = db.Column(db.String, nullable=False)
    orgname = db.Column(db.String, unique=True, nullable=False)
    orgweb = db.Column(db.String)
    venue = db.Column(db.String, nullable=False)
    startdate = db.Column(db.String, nullable=False)
    enddate = db.Column(db.String, nullable=False)
    starttime = db.Column(db.String, nullable=False)
    endtime = db.Column(db.String, nullable=False)
    logo = db.Column(db.String)
    signature = db.Column(db.String, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    ticketTemplate = db.Column(db.String, nullable=False)
    certificateTemplate= db.Column(db.String, nullable=False)
    bannerTemplate= db.Column(db.String, nullable=False)
