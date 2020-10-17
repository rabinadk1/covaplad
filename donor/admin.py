from django.contrib import admin

from .models import Disease, Donor

# Register your models here.
admin.site.register(Donor)
admin.site.register(Disease)
