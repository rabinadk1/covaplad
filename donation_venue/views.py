from django.http import HttpRequest
from django.shortcuts import render

from . import models

# Create your views here.


def get_donation_venue_list(request: HttpRequest):
    donation_venues = models.DonationVenue.objects.all().order_by("name")
    # print(donation_venues)
    context = {"donation_venues": donation_venues}
    return render(request, "donation_venues.html", context=context)


def get_donation_venue(request: HttpRequest, venue_id):
    donation_venue = models.DonationVenue.objects.get(id=venue_id)
    context = {"donation_venue": donation_venue}
    return render(request, "donation_venue.html", context=context)
