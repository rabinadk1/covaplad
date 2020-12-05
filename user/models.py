from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

from address.models import Ward

GENDER_CHOICES = {
    "M": "Male",
    "F": "Female",
    "L": "Lesbian",
    "G": "Gay",
    "B": "Bisexual",
    "T": "Transgender",
    "N": "Prefer Not To Say",
}


# Create your models here.
class User(AbstractUser):
    # !Overriding these fields because they could be blank
    first_name = models.CharField("First Name", max_length=100)
    middle_name = models.CharField("Middle Name", max_length=100, blank=True)
    last_name = models.CharField("Last Name", max_length=100)
    email = models.EmailField("email address", unique=True)

    phone_number = models.PositiveBigIntegerField(
        "Phone Number", validators=[MinValueValidator(100)]
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES.items())

    dob = models.DateField("Date of Birth")

    temporary_address = models.ForeignKey(
        Ward,
        on_delete=models.PROTECT,
        related_name="temp_user",
        verbose_name="Temporary Address",
    )
    permanent_address = models.ForeignKey(
        Ward,
        on_delete=models.PROTECT,
        related_name="perm_user",
        verbose_name="Permanent Address",
    )

    class Meta:
        constraints = (
            models.CheckConstraint(
                check=models.Q(phone_number__gte=100), name="user_phone_number_gte_100"
            ),
            models.CheckConstraint(
                check=models.Q(gender__in=GENDER_CHOICES.keys()),
                name="user_gender_in_valid_choices",
            ),
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
