from django.conf import settings
from django.db import models

from donation_venue.models import DonationVenue

# Create your models here.


class Disease(models.Model):
    name = models.CharField(max_length=100)
    icd_code = models.CharField(max_length=10, unique=True)


class Donor(models.Model):
    id = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column="id",
    )
    last_symptom_date = models.DateField("covid_last_symptom_date")

    # !Store as AB+
    blood_group = models.CharField(max_length=3)
    test_report = models.TextField(blank=True)

    height = models.DecimalField(
        "height_in_feet",
        max_digits=3,
        decimal_places=2,
    )
    weight = models.DecimalField(
        "weight_in_kg",
        max_digits=3,
        decimal_places=2,
    )

    diseases = models.ManyToManyField(Disease)
    venues = models.ManyToManyField(DonationVenue, through="DonorRegistration")

    class Meta:
        constraints = (
            models.CheckConstraint(
                check=models.Q(height__gt=0.01), name="height_gt_0.01"
            ),
            models.CheckConstraint(
                check=models.Q(weight__gt=0.01), name="weight_gt_0.01"
            ),
        )


class DonorRegistration(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    venue = models.ForeignKey(DonationVenue, on_delete=models.CASCADE)

    # ! Anything passed will be ignored with current datetime
    date_time = models.DateTimeField(auto_now=True)

    did_donation = models.BooleanField(default=False)
