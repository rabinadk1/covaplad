from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,PasswordField
from wtforms.validators import Length,DataRequired,Email


class UserRegistrationForm(FlaskForm): 
    name=StringField("Name", validators=[DataRequired(),Length(2,100)])
    username=StringField("Username", validators=[DataRequired(),Length(2,20)])
    email=StringField("Email", validators=[DataRequired(),Email()])
    password=PasswordField("Password", validators=[DataRequired(),Length(8,100)])
    confirm_password=PasswordField("Confirm Password", validators=[DataRequired(),Length(8,100)])
    address=StringField("Address", validators=[Length(2,20)])
    phone_number=IntegerField("Phone Number")
    submit = SubmitField("Sign Up")
    