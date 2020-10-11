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

    # address = db.Column(db.String(255))
    phone_number = db.Column(db.BigInteger)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    temporary_address_id = db.Column(db.Integer, db.ForeignKey("city.id"))
    permanent_address_id = db.Column(db.Integer, db.ForeignKey("city.id"))

    temporary_address = db.relationship(
        "City", backref="temporary_residents", foreign_keys=temporary_address_id
    )
    permanent_address = db.relationship(
        "City", backref="permanent_residents", foreign_keys=permanent_address_id
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


event_registration = db.Table(
    "event_registration",
    db.Column(
        "volunteer_id", db.Integer, db.ForeignKey("volunteer.id"), primary_key=True
    ),
    db.Column("event_id", db.Integer, db.ForeignKey("event.id"), primary_key=True),
)

volunteer_skills = db.Table(
    "volunteer_skills",
    db.Column(
        "volunteer_id", db.Integer, db.ForeignKey("volunteer.id"), primary_key=True
    ),
    db.Column("skill_id", db.Integer, db.ForeignKey("skill.id"), primary_key=True),
)


class Volunteer(db.Model):
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    start_date_time = db.Column(db.DateTime, nullable=False)
    end_date_time = db.Column(db.DateTime, nullable=False)
    interested_fields = db.Column(db.String(100), nullable=False)
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
    """
    Load skills immediately after loading Volunteer using subquery but do not
    load volunteers info when loading Skill
    """
    skills = db.relationship(
        "Skill",
        secondary=volunteer_skills,
        lazy="subquery",
        backref=db.backref("volunteers", lazy=True),
    )

    def __repr__(self):
        return (
            f"Volunteer(start_date_time='{self.start_date_time}', "
            f"end_date_time='{self.end_date_time}')"
        )


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    details = db.Column(db.Text(), nullable=False)
    volunteer_id = db.Column(db.Integer, db.ForeignKey("volunteer.id"), nullable=True)


class EventType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    events = db.relationship("Event", backref="eventtype", lazy=True)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)

    event_type_id = db.Column(
        db.Integer, db.ForeignKey("event_type.id"), nullable=False
    )
    city_id = db.Column(db.Integer, db.ForeignKey("city.id"), nullable="False")

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

donor_disease = db.Table(
    "donor_disease",
    db.Column("donor_id", db.Integer, db.ForeignKey("donor.id"), primary_key=True),
    db.Column("disease_id", db.Integer, db.ForeignKey("disease.id"), primary_key=True),
)


class Donor(db.Model):
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    covid_last_symptom_date = db.Column(db.Date, nullable=False)
    blood_group = db.Column(db.String(10), nullable=False)
    test_report = db.Column(db.Text())
    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)

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

    """
    Load donor_diseases when loading Donor but dont load donors info
    when loading diseases
    TODO: Check its uses and complexity later on
    """

    diseases = db.relationship(
        "Disease",
        secondary=donor_disease,
        lazy=False,
        backref=db.backref("donors", lazy=True),
    )

    def __repr__(self):
        return f"Donor(covid_last_symptom_date='{self.covid_last_symptom_date}')"


class Disease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    icd_code = db.Column(db.String(10), unique=True, nullable=False)


class DonationVenue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(su.EmailType(), unique=True, nullable=False)
    phone_number = db.Column(db.BigInteger, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey("city.id"), nullable=False)

    def __repr__(self):
        return f"DonationVenue(name='{self.name}', address='{self.address}')"


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    provinces = db.relationship("Province", backref="country", lazy=True)


class Province(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey("country.id"), primary_key=True)

    districts = db.relationship("District", backref="province", lazy=True)


class District(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    province_id = db.Column(db.Integer, db.ForeignKey("province.id"), primary_key=True)

    cities = db.relationship("City", backref="district", lazy=True)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    district_id = db.Column(db.Integer, db.ForeignKey("district.id"), nullable=False)

    venues = db.relationship("DonationVenue", backref="city", lazy=True)
    events = db.relationship(
        "Event",
        backref="city",
        lazy=True,
    )
