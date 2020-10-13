import sqlalchemy_utils as su
from flask_login import UserMixin

from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(su.EmailType(), unique=True, nullable=False)

    password = db.Column(su.PasswordType(schemes=["pbkdf2_sha512"]), nullable=False)

    # address = db.Column(db.String(255))
    phone_number = db.Column(db.BigInteger)

    # Makes database server automatically add 0 on default
    is_admin = db.Column(db.Boolean, server_default="0", nullable=False)

    temporary_address_id = db.Column(db.Integer, db.ForeignKey("ward.id"))
    permanent_address_id = db.Column(db.Integer, db.ForeignKey("ward.id"))

    temporary_address = db.relationship(
        "Ward", backref="temporary_residents", foreign_keys=temporary_address_id
    )
    permanent_address = db.relationship(
        "Ward", backref="permanent_residents", foreign_keys=permanent_address_id
    )

    """
    DONOT load Volunteer info when loading User but load user info
    when loading Volunteer and Donor
    TODO: Check its uses and complexity later on
    # """
    volunteer = db.relationship(
        "Volunteer", backref=db.backref("user", lazy=False), uselist=False
    )
    donor = db.relationship(
        "Donor", backref=db.backref("user", lazy=False), uselist=False
    )

    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}')"
