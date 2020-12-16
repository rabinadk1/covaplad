from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render

from volunteer.models import Volunteer, VolunteerRegistration

from . import models
from .models import Event

# Create your views here.


def get_event_list(request: HttpRequest):
    events = models.Event.objects.all().order_by("name")
    # print(events)
    context = {"events": events}
    return render(request, "events.html", context=context)


def get_event(request: HttpRequest, event_id):
    event = models.Event.objects.get(id=event_id)
    context = {"event": event}
    return render(request, "event.html", context=context)


@login_required
def event_registration(request: HttpRequest, event_id):
    user = request.user
    if not hasattr(user, "volunteer"):
        return redirect("volunteer_registration")
    else:
        volunteer = Volunteer.objects.get(user=user)
        event = Event.objects.get(id=event_id)
        if event not in volunteer.events.all():
            event_registration = VolunteerRegistration(volunteer=volunteer, event=event)
            event_registration.save()
        return redirect("get_event", event_id=event_id)
