"""
This file contains the model of the database
NOTE: This doesn't create an extra class and lets the statements
fall at database level. So the validation should be done before
passing to this class using wtforms or something.

! A single-column primary key that is of an INTEGER type with no
stated client-side or python-side defaults should receive auto
increment semantics automatically
"""
import sqlalchemy_utils as su
from flask_login import UserMixin

from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(su.EmailType(), unique=True, nullable=False)

    # !length assumed to be from werkzeug.security.generate_password_hash
    password = db.Column(su.PasswordType(schemes=["pbkdf2_sha512"]), nullable=False)

    address = db.Column(db.String(255))
    phone_number = db.Column(db.BigInteger)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    """
    DONOT load voluter info when loading User but load user info
    when loading Volunteer and Donor
    TODO: Check its uses and complexity later on
    # """
    voluteer = db.relationship(
        "Volunteer", backref=db.backref("user", lazy=False), uselist=False
    )
    donor = db.relationship(
        "Donor", backref=db.backref("user", lazy=False), uselist=False
    )

    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}')"


event_registration = db.Table(
    "event_registration",
    db.Column(
        "volunteer_id", db.Integer, db.ForeignKey("volunteer.id"), primary_key=True
    ),
    db.Column("event_id", db.Integer, db.ForeignKey("event.id"), primary_key=True),
)


class Volunteer(db.Model):
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    start_date_time = db.Column(db.DateTime, nullable=False)
    end_date_time = db.Column(db.DateTime, nullable=False)

    """
    DONOT load events when loading Volunteer but load volunters info
    using subquery when loading Event
    TODO: Check its uses and complexity later on
    """
    events = db.relationship(
        "Event",
        secondary=event_registration,
        backref=db.backref("volunteers", lazy="subquery"),
    )

    def __repr__(self):
        return (
            f"Volunteer(start_date_time='{self.start_date_time}', "
            f"end_date_time='{self.end_date_time}')"
        )


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    address = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return (
            f"Event(start_date_time='{self.start_date_time}', "
            f"end_date_time='{self.end_date_time}')"
        )


donation_registration = db.Table(
    "donation_registration",
    db.Column("donor_id", db.Integer, db.ForeignKey("donor.id"), primary_key=True),
    db.Column(
        "venue_id", db.Integer, db.ForeignKey("donation_venue.id"), primary_key=True
    ),
)


class Donor(db.Model):
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    covid_last_symptom_date = db.Column(db.Date, nullable=False)

    """
    DONOT load donation venues when loading Donor but load donors info
    using subquery when loading DonationVenue
    TODO: Check its uses and complexity later on
    """
    venues = db.relationship(
        "DonationVenue",
        secondary=donation_registration,
        backref=db.backref("donors", lazy="subquery"),
    )

    def __repr__(self):
        return f"Donor(covid_last_symptom_date='{self.covid_last_symptom_date}')"


class DonationVenue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(su.EmailType(), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.BigInteger, nullable=False)

    def __repr__(self):
        return f"DonationVenue(name='{self.name}', address='{self.address}')"
