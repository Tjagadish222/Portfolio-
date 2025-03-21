
import os

class Config:
    SECRET_KEY = os.environ.get("SESSION_SECRET", "dev-secret-key")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///portfolio.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
