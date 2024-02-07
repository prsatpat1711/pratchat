from db import db
from datetime import datetime
from sqlalchemy import Text
from sqlalchemy.orm import relationship


class User(db.Model):
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256))
    name = db.Column(db.String(256))
    role = db.Column(db.String(256))
    password = db.Column(db.String(256))

    # Timestamps
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # History
    archive = db.Column(db.Boolean, default=False)


    def __repr__(self):
        return f"<User {self.id}>"

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'role': self.role
        }

