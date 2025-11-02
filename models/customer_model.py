from models.user_model import db
from datetime import datetime

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    member_no = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    father_husband = db.Column(db.String(100))
    village = db.Column(db.String(100))
    post = db.Column(db.String(100))
    thana = db.Column(db.String(100))
    district = db.Column(db.String(100))
    granter = db.Column(db.String(100))
    profession = db.Column(db.String(100))
    nid_no = db.Column(db.String(50))
    admission_fee = db.Column(db.Float, default=0.0)
    address = db.Column(db.String(200))
    staff_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    total_loan = db.Column(db.Float, default=0.0)
    remaining_loan = db.Column(db.Float, default=0.0)
    savings_balance = db.Column(db.Float, default=0.0)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    staff = db.relationship('User', backref='customers')
