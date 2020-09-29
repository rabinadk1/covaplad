from datetime import datetime

from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
from wtforms.fields.html5 import DateTimeLocalField, EmailField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Length, NumberRange, Optional


class UserRegistrationForm(FlaskForm):
    name = StringField("Name", validators=[Length(2, 100)])
    username = StringField("Username", validators=[Length(2, 20)])
    email = EmailField("Email", validators=[Length(max=255)])
    password = PasswordField("Password", validators=[Length(8, 100)])
    confirm_password = PasswordField(
        "Confirm Password", validators=[EqualTo("password")]
    )
    address = StringField("Address", validators=[Optional(), Length(2, 255)])
    # phone_number = IntegerField(
    #     "Phone Number", validators=[NumberRange(100, 9999999999)]
    # )
    submit = SubmitField("Sign Up")


class EventResistrationForm(FlaskForm):
    name = StringField("Name", validators=[Length(2, 100)])
    start = DateTimeLocalField(
        "Start Date",
        default=datetime.now,
        validators=[
            DataRequired(
                "Invalid Datetime format. Please input in format ='%Y-%m-%d %H:%M:%S"
            )
        ],
    )
    end = DateTimeLocalField(
        "End Date",
        default=datetime.now,
        validators=[
            DataRequired(
                "Invalid Datetime format. Please input in format ='%Y-%m-%d %H:%M:%S"
            )
        ],
    )
    address = StringField("Address", validators=[Length(2, 255)])
    submit = SubmitField("Register Event")


class DonationVenueRegistrationForm(FlaskForm):
    name = StringField("Name", validators=[Length(2, 100)])
    email = EmailField("Email", validators=[Length(max=255)])
    address = StringField("Address", validators=[Optional(), Length(2, 255)])
    phone_number = IntegerField(
        "Phone Number", default=0, validators=[NumberRange(100, 9999999999)]
    )
    submit = SubmitField("Register Venue")
