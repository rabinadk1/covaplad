from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Username or Email Address")
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "middle_name",
            "last_name",
            "phone_number",
            "gender",
            "dob",
            "temporary_address",
            "permanent_address",
        )
        widgets = {
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }
