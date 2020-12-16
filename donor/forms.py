from datetime import date

from django import forms

from .models import Donor


class DonorForm(forms.ModelForm):
    test_reports = forms.FileField(
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
                attrs={"type": "date", "max": date.today()}
            ),
        }
