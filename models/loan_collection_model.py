from models.user_model import db
from datetime import datetime

class LoanCollection(db.Model):
    __tablename__ = 'loan_collections'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    collection_date = db.Column(db.DateTime, default=datetime.utcnow)
    staff_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    customer = db.relationship('Customer', backref='loan_collections')
    staff = db.relationship('User', backref='loan_collections')
