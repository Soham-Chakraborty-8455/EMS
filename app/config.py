import os

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///eventlabs.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')
