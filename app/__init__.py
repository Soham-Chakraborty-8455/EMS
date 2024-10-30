# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///eventlabs.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key_here')
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth_bp.login'
    
    with app.app_context():
        from .controllers.main_controller import main_bp
        from .controllers.auth_controller import auth_bp
        from .controllers.event_controller import event_bp
        from .controllers.participant_controller import participant_bp
        from .controllers.certificate_controller import certificate_bp

        app.register_blueprint(main_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(event_bp)
        app.register_blueprint(participant_bp)
        app.register_blueprint(certificate_bp)

        db.create_all()

    return app
