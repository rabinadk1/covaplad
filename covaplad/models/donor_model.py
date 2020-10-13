from datetime import datetime

from . import db

donation_registration = db.Table(
    "donation_registration",
    db.Column("donor_id", db.Integer, db.ForeignKey("donor.id"), primary_key=True),
    db.Column(
        "venue_id", db.Integer, db.ForeignKey("donation_venue.id"), primary_key=True
    ),
    # !Should be overwritten on special conditions only
    # TODO: change to server default for utc_now
    db.Column("time", db.DateTime, default=datetime.utcnow, nullable=False),
    db.Column("did_donation", db.Boolean, server_default="0", nullable=False),
)

donor_disease = db.Table(
    "donor_disease",
    db.Column("donor_id", db.Integer, db.ForeignKey("donor.id"), primary_key=True),
    db.Column("disease_id", db.Integer, db.ForeignKey("disease.id"), primary_key=True),
)


class Donor(db.Model):
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    covid_last_symptom_date = db.Column(db.Date, nullable=False)

    # !Store as AB+
    blood_group = db.Column(db.String(3), nullable=False)
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
        backref="donors",
        lazy=False,
    )

    def __repr__(self):
        return f"Donor(covid_last_symptom_date='{self.covid_last_symptom_date}')"


class Disease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    icd_code = db.Column(db.String(10), unique=True, nullable=False)
