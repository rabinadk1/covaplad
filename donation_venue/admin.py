from django.contrib import admin

from django.urls import reverse
from django.utils.html import mark_safe
from .models import DonationVenue
from donor.models import DonorRegistration


class DonorRegistrationInline(admin.TabularInline):
    model = DonorRegistration
    extra = 0
    readonly_fields = 'link',

    def link(self, instance):
        url = reverse("admin:donor_donor_change", args=(instance.id,))
        return mark_safe("<a href='%s'>%s</a>" % (url, instance))

    # show_change_link = True


class DonationVenueAdmin(admin.ModelAdmin):
    inlines = (DonorRegistrationInline,)


# Register your  models here
admin.site.register(DonationVenue, DonationVenueAdmin)
