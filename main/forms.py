from django import forms

# from . import models


class LoginForm(forms.Form):
    username = forms.CharField(label="Username or Email Address")
    password = forms.CharField(widget=forms.PasswordInput)
