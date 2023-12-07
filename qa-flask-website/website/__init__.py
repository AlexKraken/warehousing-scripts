from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
DB_NAME = "barcodes.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("MY_APP_SECRET_KEY", "default_secret_key_0123456789ABCDEF")
    print(os.environ.get("MY_APP_SECRET_KEY", "default_secret_key_0123456789ABCDEF"))
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    from .models import Barcode

    with app.app_context():
        db.create_all()

    return app
