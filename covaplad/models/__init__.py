"""
This package contains the model of the database
NOTE: This doesn't create an extra class and lets the statements
fall at database level. So the validation should be done before
passing to this class using wtforms or something.

! A single-column primary key that is of an INTEGER type with no
stated client-side or python-side defaults should receive auto
increment semantics automatically
"""

from .. import db  # noqa
from .address_model import Country, District, Municipality, Province, Ward  # noqa
from .donation_venue_model import DonationVenue  # noqa
from .donor_model import Disease, Donor  # noqa
from .event_model import Event, EventType  # noqa
from .user_model import User  # noqa
from .volunteer_model import Skill, Volunteer  # noqa
