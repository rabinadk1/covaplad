from django.contrib import admin

from .models import Country, District, Municipality, Province, Ward

# Register your models here.
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Municipality)
admin.site.register(Ward)
