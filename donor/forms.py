from django import forms

from .models import Donor


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = [
            "height",
            "weight",
            "blood_group",
            "last_symptom_date",
            "test_report",
            "diseases",
        ]

        widgets = {"diseases": forms.SelectMultiple()}
