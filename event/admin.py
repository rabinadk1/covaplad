from django.contrib import admin

from django.urls import reverse
from django.utils.html import mark_safe

from .models import Event, EventType
from volunteer.models import VolunteerRegistration


class VolunteerRegistrationInline(admin.TabularInline):
    model = VolunteerRegistration
    extra = 0
    readonly_fields = ("link",)

    def link(self, instance):
        url = reverse("admin:volunteer_volunteer_change", args=(instance.id,))
        return mark_safe("<a href='%s'>%s</a>" % (url, instance))

    # show_change_link = True


class EventAdmin(admin.ModelAdmin):
    inlines = (VolunteerRegistrationInline,)


# Register your models here
admin.site.register(Event, EventAdmin)
admin.site.register(EventType)
