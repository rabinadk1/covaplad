from django import forms

from .models import Volunteer


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = [
            "start_date_time",
            "end_date_time",
            "interested_fields",
            "skills",
        ]
