from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.bootstrap import bootstrap_services
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    
    app.config.from_object('config.config.Config')

    bootstrap_services(app)

    return app
