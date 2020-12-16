from datetime import date, timedelta

from django import forms

from .models import Donor


class DonorForm(forms.ModelForm):
    test_reports = forms.FileField(
        label="Test Reports",
        widget=forms.ClearableFileInput(attrs={"multiple": True, "accept": "image/*"}),
        required=False,
    )

    class Meta:
        model = Donor
        fields = [
            "height",
            "weight",
            "blood_group",
            "last_symptom_date",
            "diseases",
        ]

        widgets = {
            "last_symptom_date": forms.widgets.DateInput(
                attrs={
                    "type": "date",
                    "min": lambda: date.today() - timedelta(28),
                    "max": date.today,
                }
            ),
        }
