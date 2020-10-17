from django.db import models

from address.models import Ward


# Create your models here.
class EventType(models.Model):
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField()

    class Meta:
        verbose_name = "Event Type"


class Event(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

    event_type = models.ForeignKey(
        EventType, on_delete=models.PROTECT, verbose_name="Event Type"
    )

    address = models.ForeignKey(Ward, on_delete=models.CASCADE)
