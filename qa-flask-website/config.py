import os


class Config:
    DB_NAME = "barcodes.db"
    SECRET_KEY = os.environ.get("SECRET_KEY", "default_secret_key_0123456789ABCDEF")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
