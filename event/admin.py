from django.contrib import admin

from .models import Event, EventType

# Register your models here.
admin.site.register(Event)
admin.site.register(EventType)
