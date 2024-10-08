from flask import Blueprint, request, jsonify, render_template
from ..models.event import EventDetails
from ..services.banner_service import create_banner
from ..services.email_service import send_registration_email
from .. import db

event_bp = Blueprint('event_bp', __name__)

@event_bp.route("/eventdetails", methods=["GET", "POST"])
def event_data():
    if request.method == "POST":
        data = request.json
        event = EventDetails(**data)
        db.session.add(event)
        db.session.commit()

        create_banner(data['bannerTemplate'], data['orgname'], data['eventname'], data['venue'], data['startdate'], data['starttime'])
        send_registration_email()

        return jsonify({'eventid': event.id})

    # return render_template('../template/index.html')
