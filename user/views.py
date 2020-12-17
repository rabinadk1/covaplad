from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render

from address.forms import AddressForm
from event import models

from . import forms

# Create your views here.


def home(request: HttpRequest):
    events = models.Event.objects.all().order_by("name")
    # print(events)
    context = {"events": events}
    return render(request, "home.html", context=context)


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
