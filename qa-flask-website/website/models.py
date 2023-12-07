from . import db
from sqlalchemy.sql import func


class Barcode(db.Model):
    barcode = db.Column(db.String(20), primary_key=True)
    notes = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
