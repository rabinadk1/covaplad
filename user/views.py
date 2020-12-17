from datetime import datetime

from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render

from address.forms import AddressForm
from donation_venue import models as dvmodels
from event import models as evmodels

from . import forms

# Create your views here.


def home(request: HttpRequest):
    if request.user.is_authenticated:
        events = evmodels.Event.objects.filter(end__gte=datetime.now()).order_by(
            "-end", "name"
        )[:3]
        donation_venues = dvmodels.DonationVenue.objects.order_by("name")[:3]
        context = {"events": events, "donation_venues": donation_venues}
        return render(request, "dashboard.html", context=context)
    else:
        events = evmodels.Event.objects.filter(end__gte=datetime.now()).order_by(
            "-end", "name"
        )[:3]
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
