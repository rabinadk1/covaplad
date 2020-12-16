from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_event_list, name="get_event_list"),
    path("<int:event_id>", views.get_event, name="get_event"),
    path(
        "<int:event_id>/register", views.event_registration, name="event_registration"
    ),
]
