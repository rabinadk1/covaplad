from datetime import datetime

from . import db

event_registration = db.Table(
    "event_registration",
    db.Column(
        "volunteer_id", db.Integer, db.ForeignKey("volunteer.id"), primary_key=True
    ),
    db.Column("event_id", db.Integer, db.ForeignKey("event.id"), primary_key=True),
    # !Should be overwritten on special conditions only
    # TODO: change to server default for utc_now
    db.Column("time", db.DateTime, default=datetime.utcnow, nullable=False),
    db.Column("was_present", db.Boolean, server_default="0", nullable=False),
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
    Load skills immediately after loading Volunteer but do not
    load volunteers info when loading Skill
    """
    skills = db.relationship(
        "Skill", secondary=volunteer_skills, lazy="subquery", backref="volunteers"
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
