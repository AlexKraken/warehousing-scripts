import os


class Config:
    """Stores the configuration variables for the application.
    Import them using
        `app.config.from_object(Config)`
    """

    # Secret key for cryptographic operations
    SECRET_KEY = os.environ.get("SECRET_KEY", "default_secret_key_0123456789ABCDEF")

    # SameSite attribute and secure flag for session cookies
    SESSION_COOKIE_SAMESITE = "None"
    SESSION_COOKIE_SECURE = True

    # Database configuration for Flask-SQLAlchemy
    DB_NAME = "barcodes.db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
