from datetime import datetime

from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, PasswordField, StringField, SubmitField
from wtforms.fields.html5 import DateTimeLocalField, EmailField, TelField
from wtforms.validators import DataRequired, EqualTo, Length, Optional, ValidationError

from .models import User


class UserRegistrationForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[DataRequired("Please enter your full name."), Length(2, 100)],
    )
    username = StringField(
        "Username",
        validators=[
            DataRequired("Please enter a username. The length can not be less than 4."),
            Length(4, 20),
        ],
    )
    email = EmailField(
        "Email",
        validators=[
            DataRequired("Please enter a vallid email address."),
            Length(max=255),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired("Please enter a password."),
            Length(min=8, max=100, message="Please enter a stronger password."),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[EqualTo("password", message="Passwords donot match.")],
    )
    address = StringField("Address", validators=[Optional(), Length(2, 255)])
    phone_number = TelField("Phone Number", validators=[Optional()])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).one_or_none()
        if user is not None:
            raise ValidationError(
                "This username is taken. Please choose a different one."
            )

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).one_or_none()
        if user is not None:
            raise ValidationError(
                "This email is taken. Try another email. "
                "If it is your email, contact us."
            )


class LoginForm(FlaskForm):
    """User log in form"""

    email = EmailField(
        "Email",
        validators=[
            DataRequired("Please enter a vallid email address."),
        ],
    )
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Log In")


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
    address = StringField("Address", validators=[Length(2, 255)])
    phone_number = TelField("Phone Number", validators=[DataRequired()])
    submit = SubmitField("Register Venue")
