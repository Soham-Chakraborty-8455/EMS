# app/routes/event_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from flask_login import login_required
from ..models.models import EventDetails
from ..services.banner_service import create_banner
from ..services.email_service import send_registration_email
from .. import db

event_bp = Blueprint('event_bp', __name__)

@event_bp.route("/create_event", methods=["GET", "POST"])
@login_required
def create_event():
    if request.method == "POST":
        data = request.json
        new_event = EventDetails(
            eventname=data['eventname'],
            orgname=data['orgname'],
            orgweb=data.get('orgweb', ''),
            venue=data['venue'],
            startdate=data['startdate'],
            enddate=data['enddate'],
            starttime=data['starttime'],
            endtime=data['endtime'],
            logo=data.get('logo', ''),
            signature=data['signature'],
            cost=data['cost'],
            ticketTemplate=data['ticketTemplate'],
            certificateTemplate=data['certificateTemplate'],
            bannerTemplate=data['bannerTemplate']
        )
        db.session.add(new_event)
        db.session.commit()

        create_banner(
            data['bannerTemplate'],
            data['orgname'],
            data['eventname'],
            data['venue'],
            data['startdate'],
            data['starttime']
        )
        # send_registration_email()

        return jsonify({'eventid': new_event.id}), 201

    return render_template('create_event.html')
