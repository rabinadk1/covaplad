from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.shortcuts import redirect, render

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
    form = forms.SignupForm(request.POST or None)
    if form.is_valid():
        messages.info(request, "You have registered successfully. Login to continue.")
        form.save()
        return redirect("login")

    return render(
        request,
        "signup.html",
        {"form": form},
    )
