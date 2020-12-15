from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.shortcuts import redirect, render

from address.forms import AddressForm

from . import forms

# Create your views here.


def home(request: HttpRequest):
    return render(request, "home.html")


def login_user(request: HttpRequest):
    form = forms.LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password) or authenticate(
            email=username, password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, message="Invalid username/email or password.")

    return render(request, "login.html", {"form": form})


def logout_user(request: HttpRequest):
    logout(request)
    messages.info(request, "Successfully logged out")
    return redirect("home")


def register_user(request: HttpRequest):
    signup_form = forms.SignupForm(request.POST or None)
    temporary_address_form = AddressForm(request.POST or None, prefix="temporary")
    permanent_address_form = AddressForm(request.POST or None, prefix="permanent")
    print(temporary_address_form.is_valid())
    if (
        signup_form.is_valid()
        and temporary_address_form.is_valid()
        and permanent_address_form.is_valid()
    ):
        messages.info(request, "You have registered successfully. Login to continue.")
        signup = signup_form.save(False)
        signup.temporary_address = temporary_address_form.cleaned_data.get("ward")
        signup.permanent_address = permanent_address_form.cleaned_data.get("ward")
        signup.save()
        return redirect("login")

    return render(
        request,
        "signup.html",
        {
            "signup_form": signup_form,
            "temporary_address_form": temporary_address_form,
            "permanent_address_form": permanent_address_form,
        },
    )
