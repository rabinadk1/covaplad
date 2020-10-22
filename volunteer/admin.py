from django.contrib import admin

from .models import Skill, Volunteer

# Register your models here.
admin.site.register(Volunteer)
admin.site.register(Skill)
