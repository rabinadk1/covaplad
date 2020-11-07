from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "middle_name", "last_name", "email"]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {"fields": ("first_name", "middle_name", "last_name", "email")},
        ),
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
        (None, {"fields": ("username", "password1", "password2", "email")}),
        (
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
        ),
        (
            "Address Information",
            {
                "fields": (
                    "temporary_address",
                    "permanent_address",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
