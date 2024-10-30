# app/routes/main_routes.py (updated)

from flask import Blueprint, render_template
from ..models.models import EventDetails
from flask_login import current_user

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def home():
    events = EventDetails.query.all()
    return render_template('index.html', events=events)
