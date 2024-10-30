from flask import Blueprint, request, jsonify, render_template
from ..models.event import EventDetails
from ..models.participant import Participants, Certificate
from ..services.email_service import send_registration_email
from ..utils.csv_utils import write_to_csv
from ..services.ticket_service import create_ticket
from ..services.certificate_service import create_certificate
from .. import db

participant_bp = Blueprint('participant_bp', __name__)

@participant_bp.route("/participantdetails", methods=["GET", "POST"])
def participants():
    if request.method == 'POST':
        data = request.json
        write_to_csv('participantList.csv', data)

        registration = Participants(
            eventid=int(data['eventid']),
            eventname=data['eventname'],
            email=data['email'],
            name=data['name'],
            phone=int(data['phone']),
            address=data['address']
        )
        db.session.add(registration)
        db.session.commit()

        event_details = EventDetails.query.filter_by(id=data['eventid']).first()
        create_ticket(event_details.ticketTemplate, registration, event_details)

        return jsonify({'trigger': True})

    return render_template('participant_details.html')

@participant_bp.route("/checkout", methods=["GET", "POST"])
def checkin():
    if request.method == 'POST':
        data = request.json
        write_to_csv('FinalAttendee.csv', data)

        certlist = Certificate(**data)
        db.session.add(certlist)
        db.session.commit()

        event_details = EventDetails.query.filter_by(id=data['eventid']).first()
        create_certificate(event_details.certificateTemplate, data, event_details)

        return jsonify({'status': 'Certificate created'})

    return render_template('checkout.html')
