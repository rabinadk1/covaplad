from django.core.validators import MinValueValidator
from django.db import models

from address.models import Ward


# Create your models here.
class DonationVenue(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.PositiveBigIntegerField(
        "Phone Number", validators=[MinValueValidator(100)]
    )

    address = models.ForeignKey(Ward, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Donation Venue"

        # !There cannot be donation venue with same name in same ward
        constraints = (
            models.UniqueConstraint(
                fields=("name", "address"), name="donationvenue_unique_name_address"
            ),
            models.CheckConstraint(
                check=models.Q(phone_number__gte=100),
                name="donationvenue_phone_number_gte_100",
            ),
        )

    def __str__(self):
        return f"{self.name}, {self.address}"
