from django.db import models

from address.models import Ward


# Create your models here.
class DonationVenue(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.BigIntegerField()

    address = models.ForeignKey(Ward, on_delete=models.CASCADE)
