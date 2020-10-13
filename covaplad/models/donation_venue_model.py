import sqlalchemy_utils as su

from . import db


class DonationVenue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(su.EmailType(), unique=True, nullable=False)
    phone_number = db.Column(db.BigInteger, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey("ward.id"), nullable=False)

    address = db.relationship("Ward", backref="venues")

    def __repr__(self):
        return f"DonationVenue(name='{self.name}', address='{self.address}')"
