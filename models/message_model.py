from models.user_model import db
from datetime import datetime

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    is_read = db.Column(db.Boolean, default=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    staff = db.relationship('User', backref='messages')
