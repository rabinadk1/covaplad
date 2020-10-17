from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models

from address.models import Ward


# Create your models here.
class User(AbstractUser):
    phone_number = models.BigIntegerField()
    gender = models.CharField(
        max_length=1,
        choices=[
            ("M", "Male"),
            ("W", "Woman"),
            ("L", "Lesbian"),
            ("G", "Gay"),
            ("B", "Bisexual"),
            ("T", "Transgender"),
            ("N", "Prefer Not To Say"),
        ],
    )

    dob = models.DateField("date_of_birth")

    temporary_address = models.ForeignKey(
        Ward, on_delete=models.PROTECT, related_name="temp_user"
    )
    permanent_address = models.ForeignKey(
        Ward, on_delete=models.PROTECT, related_name="perm_user"
    )

    @property
    def age(self):
        # Provides approx. age by assuming 365 days per year
        return (date.today() - self.dob).days // 365
