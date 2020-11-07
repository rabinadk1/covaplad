from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Extract common fields outside
personal_info = (
    "Personal Information",
    {
        "classes": ("wide"),
        "fields": (
            "first_name",
            "middle_name",
            "last_name",
            "phone_number",
            "gender",
            "dob",
        ),
    },
)
address_info = (
    "Address Information",
    {
        "fields": (
            "temporary_address",
            "permanent_address",
        )
    },
)


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        personal_info,
        address_info,
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {"fields": ("username", "email", "password1", "password2")}),
        personal_info,
        address_info,
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
