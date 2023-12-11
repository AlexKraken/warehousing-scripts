from . import db
from sqlalchemy.sql import func
from datetime import datetime
from typing import Optional


class Barcode(db.Model):
    id: str = db.Column(db.String(20), primary_key=True)
    notes: str = db.Column(db.String(1000))
    date: datetime = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self, id: str, notes: Optional[str] = None, date: Optional[datetime] = None) -> None:
        self.id = id
        self.notes = notes
        self.date = date or func.now()
