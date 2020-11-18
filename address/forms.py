from django import forms

from . import models


class AddressForm(forms.Form):
    country = forms.ModelChoiceField(models.Country.objects.only("name"))
    province = forms.ModelChoiceField(models.Province.objects.only("name"))
    district = forms.ModelChoiceField(models.District.objects.only("name"))
    municipality = forms.ModelChoiceField(
        models.Municipality.objects.only("name", "is_rural")
    )
    ward = forms.ModelChoiceField(models.Ward.objects.only("number"))
