from datetime import datetime

from django import forms

from .models import Volunteer


class VolunteerForm(forms.ModelForm):
    class Meta:
        def getCurrentDateTime():
            return datetime.now().isoformat(timespec="minutes")

        model = Volunteer
        fields = [
            "start_date_time",
            "end_date_time",
            "interested_fields",
            "skills",
        ]

        widgets = {
            "start_date_time": forms.widgets.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "max": getCurrentDateTime,
                }
            ),
            "end_date_time": forms.widgets.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "max": getCurrentDateTime,
                }
            ),
        }
