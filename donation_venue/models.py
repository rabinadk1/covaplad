from django.db import models

from address.models import Ward


# Create your models here.
class DonationVenue(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.BigIntegerField("Phone Number")

    address = models.ForeignKey(Ward, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Donation Venue"

        # !There cannot be donation venue with same name in same ward
        constraints = (
            models.UniqueConstraint(
                fields=("name", "address"), name="unique_name_address"
            ),
        )

    def __str__(self):
        return f"{self.name}, {self.address}"
