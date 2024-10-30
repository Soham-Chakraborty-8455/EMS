from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        # Import and register blueprints
        from .controllers.event_controller import event_bp
        from .controllers.participant_controller import participant_bp
        from .controllers.main_controller import main_bp

        app.register_blueprint(main_bp)
        app.register_blueprint(event_bp)
        app.register_blueprint(participant_bp)

        db.create_all()

    return app
