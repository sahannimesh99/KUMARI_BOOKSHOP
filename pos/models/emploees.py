# pos/models/emploees.py
from pos.models import db

class Emploees(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    nic = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(45), nullable=False)
    contact = db.Column(db.Integer, nullable=False)
