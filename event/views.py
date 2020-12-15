# from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.shortcuts import render

from . import models


def get_event_list(request: HttpRequest):
    events = models.Event.objects.all().order_by("name")
    # print(events)
    context = {"events": events}
    return render(request, "events.html", context=context)


def get_event(request: HttpRequest, venue_id):
    event = models.Event.objects.get(id=venue_id)
    context = {"event": event}
    return render(request, "event.html", context=context)
