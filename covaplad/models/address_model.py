from . import db


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    provinces = db.relationship("Province", backref="country")


class Province(db.Model):
    # !Assuming a country cannot have provinces of same name
    __table_args__ = (db.UniqueConstraint("name", "country_id"),)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey("country.id"), nullable=False)

    districts = db.relationship("District", backref="province")


class District(db.Model):
    # !Assuming a province cannot have districts of same name
    __table_args__ = (db.UniqueConstraint("name", "province_id"),)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    province_id = db.Column(db.Integer, db.ForeignKey("province.id"), nullable=False)

    municipalities = db.relationship("Municipality", backref="district")


class Municipality(db.Model):
    # !Assuming a district cannot have municipality of same name
    __table_args__ = (db.UniqueConstraint("name", "district_id"),)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    district_id = db.Column(db.Integer, db.ForeignKey("district.id"), nullable=False)

    wards = db.relationship("Ward", backref="municipality")


class Ward(db.Model):
    __table_args__ = (db.UniqueConstraint("number", "municipality_id"),)

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)

    name = db.Column(db.String(100))
    municipality_id = db.Column(
        db.Integer, db.ForeignKey("municipality.id"), nullable=False
    )
