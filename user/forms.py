from datetime import date

from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Column, Div, Layout
from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username or Email Address",
        widget=forms.TextInput(
            attrs={"placeholder": "username", "class": "form-control"}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "password", "class": "form-control"}
        )
    )


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
        )
        widgets = {
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
            "dob": forms.widgets.DateInput(attrs={"type": "date", "max": date.today}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<p class="h5 pb-3 text-primary text-center">Vital Information</h2>'),
            Div(
                Column("email", css_class="form-group col-md-6 mb-1"),
                Column("username", css_class="form-group col-md-6 mb-1"),
                css_class="row",
            ),
            Div(
                Column("password1", css_class="form-group col-md-6 mb-1"),
                Column("password2", css_class="form-group col-md-6 mb-1"),
                css_class="row",
            ),
            HTML(
                """
                <hr/>
                <p class="h5 pb-3 text-primary text-center">Personal Information</h2>
            """
            ),
            Div(
                Column("first_name", css_class="form-group col-md-4 mb-1"),
                Column("middle_name", css_class="form-group col-md-4 mb-1"),
                Column("last_name", css_class="form-group col-md-4 mb-1"),
                css_class="row",
            ),
            Div(
                Column("gender", css_class="form-group col-md-4 mb-1"),
                Column("dob", css_class="form-group col-md-4 mb-1"),
                Column("phone_number", css_class="form-group col-md-4 mb-1"),
                css_class="row",
            ),
        )
