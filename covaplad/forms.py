from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import EqualTo, Length, Optional


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
