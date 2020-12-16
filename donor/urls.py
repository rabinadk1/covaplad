from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.donor_registration, name="donor_registration"),
    path("", views.donor, name="donor"),
]
