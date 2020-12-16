from django.db import models

from address.models import Ward


# Create your models here.
class EventType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Event Type"

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)

    start = models.DateTimeField()
    end = models.DateTimeField()
    details = models.TextField(default="")

    event_type = models.ForeignKey(
        EventType, on_delete=models.PROTECT, verbose_name="Event Type"
    )

    address = models.ForeignKey(Ward, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.id})"
