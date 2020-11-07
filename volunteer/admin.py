from django.contrib import admin

from .models import Skill, Volunteer, VolunteerRegistration

# Register your models here.
admin.site.register(Skill)
admin.site.register(Volunteer)
admin.site.register(VolunteerRegistration)
