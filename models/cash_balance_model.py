from models.user_model import db
from datetime import datetime

class CashBalance(db.Model):
    __tablename__ = 'cash_balance'
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float, default=0.0)
    updated_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
