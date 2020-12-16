from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_donation_venue_list, name="get_donation_venue_list"),
    path("<int:venue_id>", views.get_donation_venue, name="get_donation_venue"),
    path(
        "<int:venue_id>/register",
        views.donation_venue_registration,
        name="donation_venue_registration",
    ),
]
