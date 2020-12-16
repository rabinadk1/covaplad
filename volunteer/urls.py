from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.volunteer_registration, name="volunteer_registration")
]
