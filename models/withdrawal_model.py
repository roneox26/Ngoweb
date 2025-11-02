from models.user_model import db
from datetime import datetime

class Withdrawal(db.Model):
    __tablename__ = 'withdrawals'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    investor_name = db.Column(db.String(100))
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    note = db.Column(db.String(200))
    withdrawal_type = db.Column(db.String(20), default='savings')
    customer = db.relationship('Customer', backref='withdrawals')
