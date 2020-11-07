from django.contrib import admin

from .models import Disease, Donor, DonorRegistration

# Register your models here.
admin.site.register(Donor)
admin.site.register(Disease)
admin.site.register(DonorRegistration)
