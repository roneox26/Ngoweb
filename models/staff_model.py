from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Staff(db.Model):
    __tablename__ = 'staffs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    position = db.Column(db.String(100), nullable=True)
    join_date = db.Column(db.DateTime, default=datetime.utcnow)
    salary = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f"<Staff {self.name}>"
