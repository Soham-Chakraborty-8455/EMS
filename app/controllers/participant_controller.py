# app/routes/participant_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from ..models.models import EventDetails, Participants
from ..services.email_service import send_registration_email
from ..services.ticket_service import create_ticket
from ..utils.csv_utils import write_to_csv
from .. import db

participant_bp = Blueprint('participant_bp', __name__)

@participant_bp.route("/register_event/<int:event_id>", methods=["GET", "POST"])
def register_event(event_id):
    event = EventDetails.query.get_or_404(event_id)

    if request.method == 'POST':
        data = request.json
        participant = Participants(
            eventid=event.id,
            eventname=event.eventname,
            email=data['email'],
            name=data['name'],
            phone=data['phone'],
            address=data['address']
        )
        db.session.add(participant)
        db.session.commit()

        write_to_csv('participantList.csv', data)
        create_ticket(event.ticketTemplate, participant, event)

        send_registration_email(participant.email, event)

        return jsonify({'status': 'Registration successful'}), 201

    return render_template('participant_registration.html', event=event)
