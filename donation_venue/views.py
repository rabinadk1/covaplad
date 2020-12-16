from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render

from donor.models import Donor, DonorRegistration

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


@login_required
def donation_venue_registration(request: HttpRequest, venue_id):
    user = request.user
    if not hasattr(user, "donor"):
        return redirect("donor_registration")
    else:
        donor = Donor.objects.get(user=user)
        donation_venue = models.DonationVenue.objects.get(id=venue_id)
        if donation_venue in donor.venues.all():
            print("Registered in the venue.")
        else:
            donation_venue_registration = DonorRegistration(
                donor=donor, venue=donation_venue
            )
            donation_venue_registration.save()
        return redirect("get_donation_venue", venue_id=venue_id)
