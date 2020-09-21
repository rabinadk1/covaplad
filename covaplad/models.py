"""
This file contains the model of the database
NOTE: This doesn't create an extra class and lets the statements
fall at database level. So the validation should be done before
passing to this class using wtforms or something.
"""

from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    # !length assumed to be from werkzeug.security.generate_password_hash
    password = db.Column(db.String(94), unique=True, nullable=False)

    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}')"


if __name__ == "__main__":
    db.create_all()
