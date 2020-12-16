from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render

from . import forms

# Create your views here.


def home(request: HttpRequest):
    return render(request, "home.html")


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
