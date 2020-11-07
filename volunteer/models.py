from django.conf import settings
from django.db import models

from event.models import Event

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    details = models.TextField()

    def __str__(self):
        return self.name


class Volunteer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column="id",
        verbose_name="ID",
    )
    start_date_time = models.DateTimeField("Start Date Time")
    end_date_time = models.DateTimeField("End Date Time")
    interested_fields = models.CharField(
        "Interested Fields", max_length=100, blank=True
    )

    skills = models.ManyToManyField(Skill)
    events = models.ManyToManyField(Event, through="VolunteerRegistration")

    def __str__(self):
        return self.user.username


class VolunteerRegistration(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    was_present = models.BooleanField(
        "Check if the volunteer was present on the event", default=False
    )

    # ! Anything passed will be ignored with current datetime
    date_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Volunteer Registration"
