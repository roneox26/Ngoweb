from models.user_model import db
from datetime import datetime

class Collection(db.Model):
    __tablename__ = 'collections'
    id = db.Column(db.Integer, primary_key=True)
    loan_id = db.Column(db.Integer, db.ForeignKey('loans.id'))
    amount = db.Column(db.Float, nullable=False)
    collection_date = db.Column(db.DateTime, default=datetime.utcnow)
    staff_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    loan = db.relationship('Loan', backref='collections')
    staff = db.relationship('User', backref='collections')
