from django.contrib.auth.models import User
from django.db import models

from event.models import Event

# Create your models here.


class Skill(models.Model):
    name = models.CharField(
        max_length=100,
    )
    details = models.TextField()


class Volunteer(models.Model):
    id = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, db_column="id"
    )
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    interested_fields = models.CharField(max_length=100, blank=True)

    skills = models.ManyToManyField(Skill)
    events = models.ManyToManyField(Event, through="VolunteerRegistration")


class VolunteerRegistration(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    # ! Anything passed will be ignored with current datetime
    date_time = models.DateTimeField(auto_now=True)

    was_present = models.BooleanField(default=False)
