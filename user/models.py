from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models

from address.models import Ward


# Create your models here.
class User(AbstractUser):
    # !Overriding these fields because they could be blank
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField("email address")

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

    # ! Overriden to incorporate middle_name
    def get_full_name(self):
        """
        If middle_name is available,
        return the first_name plus the middle_name plus the last_name,
        with spaces among them.

        Else,
        return the first_name plus the middle_name plus the last_name,
        with a space in between.
        """
        _fn = self.first_name.strip()
        _mn = self.middle_name.strip()
        if _mn:
            _fn = f"{_fn} {_mn}"
        return f"{_fn} {self.last_name.strip()}".rstrip()

    @property
    def age(self):
        # Provides approx. age by assuming 365 days per year
        return (date.today() - self.dob).days // 365
