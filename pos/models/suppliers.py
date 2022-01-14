# pos/models/suppliers.py
from pos.models import db

class Suppliers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    proName = db.Column(db.String(105), nullable=False)
    nic = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(45), nullable=False)
    contact = db.Column(db.Integer, nullable=False)
