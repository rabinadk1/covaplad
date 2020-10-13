from . import db


class EventType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    events = db.relationship("Event", backref="event_type")


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)

    event_type_id = db.Column(
        db.Integer, db.ForeignKey("event_type.id"), nullable=False
    )
    address_id = db.Column(db.Integer, db.ForeignKey("ward.id"), nullable=False)

    address = db.relationship("Ward", backref="events")

    def __repr__(self):
        return (
            f"Event(start_date_time='{self.start_date_time}', "
            f"end_date_time='{self.end_date_time}')"
        )
