from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

from donation_venue.models import DonationVenue

# Create your models here.


class Disease(models.Model):
    name = models.CharField(max_length=100)
    icd_code = models.CharField("ICD Code", max_length=10, unique=True)

    def __str__(self):
        return f"{self.icd_code} ({self.name})"


class Donor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column="id",
        verbose_name="ID",
    )
    last_symptom_date = models.DateField("COVID Last Symptom Date")

    # !Store as AB+
    blood_group = models.CharField("Blood Group", max_length=3)

    height = models.DecimalField(
        "height (in feet)",
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0.02)],
    )
    weight = models.DecimalField(
        "weight (in kg)",
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0.02)],
    )

    diseases = models.ManyToManyField(Disease, blank=True)
    venues = models.ManyToManyField(DonationVenue, through="DonorRegistration")

    class Meta:
        constraints = (
            models.CheckConstraint(
                check=models.Q(height__gt=0.01), name="donor_height_gt_0.01"
            ),
            models.CheckConstraint(
                check=models.Q(weight__gt=0.01), name="donor_weight_gt_0.01"
            ),
        )

    def __str__(self):
        return self.user.username


class DonorRegistration(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    venue = models.ForeignKey(DonationVenue, on_delete=models.CASCADE)
    did_donation = models.BooleanField(
        "Check if the donor donated on the venue", default=False
    )

    # ! Anything passed will be ignored with current datetime
    date_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["donor", "venue"]
        verbose_name = "Donor Registration"


class TestReport(models.Model):
    def donor_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/donor_<id>/<filename>
        return f"donor_{instance.donor_id}/{filename}"

    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    report = models.ImageField(upload_to=donor_directory_path, unique=True)

    class Meta:
        verbose_name = "Test Report"

    def __str__(self):
        return self.report
