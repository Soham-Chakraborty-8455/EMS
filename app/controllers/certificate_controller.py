# app/routes/certificate_routes.py

from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required
from ..models.models import EventDetails, Certificate, Participants
from ..services.certificate_service import create_certificate
from ..utils.csv_utils import write_to_csv
from .. import db

certificate_bp = Blueprint('certificate_bp', __name__)

@certificate_bp.route("/checkout", methods=["GET", "POST"])
@login_required
def checkout():
    if request.method == 'POST':
        data = request.json
        participant = Participants.query.filter_by(email=data['email'], eventid=data['eventid']).first()
        if not participant:
            return {'status': 'Participant not found'}, 404

        new_certificate = Certificate(
            eventid=participant.eventid,
            eventname=participant.eventname,
            participant_id=participant.id,
            certificateTemplate=data['certificateTemplate']
        )
        db.session.add(new_certificate)
        db.session.commit()

        write_to_csv('FinalAttendee.csv', data)
        create_certificate(new_certificate.certificateTemplate, participant, participant.event)

        return jsonify({'status': 'Certificate created'}), 201

    return render_template('checkout.html')
