from django.contrib import admin

from .models import DonationVenue
from donor.models import DonorRegistration


class DonorRegistrationInline(admin.TabularInline):
    model = DonorRegistration
    extra = 1


class DonationVenueAdmin(admin.ModelAdmin):
    inlines = (DonorRegistrationInline,)


admin.site.register(DonationVenue, DonationVenueAdmin)
