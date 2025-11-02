from models.user_model import db
from datetime import datetime

class Loan(db.Model):
    __tablename__ = 'loans'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    interest = db.Column(db.Float, default=0.0)
    loan_date = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=False)
    installment_count = db.Column(db.Integer, default=0)
    installment_amount = db.Column(db.Float, default=0.0)
    service_charge = db.Column(db.Float, default=0.0)
    welfare_fee = db.Column(db.Float, default=0.0)
    installment_type = db.Column(db.String(50))
    status = db.Column(db.String(20), default='Pending')  # Pending or Paid
    staff_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    staff = db.relationship('User', backref='loans')
