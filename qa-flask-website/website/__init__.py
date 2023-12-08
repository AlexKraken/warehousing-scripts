from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os

db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    from .models import Barcode

    with app.app_context():
        db.create_all()

    return app
