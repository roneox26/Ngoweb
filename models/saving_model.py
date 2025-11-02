from models.user_model import db
from datetime import datetime

class Saving(db.Model):
    __tablename__ = 'savings'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    saving_date = db.Column(db.DateTime, default=datetime.utcnow)
    staff_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    staff = db.relationship('User', backref='savings')
