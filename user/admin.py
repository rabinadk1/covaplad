from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.

_fieldsets = list(UserAdmin.fieldsets)

_fieldsets.insert(
    2,
    (
        "Extra Fields",
        {
            "fields": (
                "phone_number",
                "gender",
                "dob",
                "temporary_address",
                "permanent_address",
            )
        },
    ),
)

_fieldsets[1][1]["fields"] = (
    "first_name",
    "middle_name",
    "last_name",
    "email",
)

UserAdmin.fieldsets = _fieldsets

admin.site.register(User, UserAdmin)
