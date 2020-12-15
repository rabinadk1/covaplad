from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Column, Div, Field, Layout, Row, Submit
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Column('country', css_class='form-group col-md-6 mb-1'),
                Column('province', css_class='form-group col-md-6 mb-1'),
                css_class='row'
            ),
             Div(
                Column('district', css_class='form-group col-md-6 mb-1'),
                Column('municipality', css_class='form-group col-md-6 mb-1'),
                css_class='row'
            ),
              Div(
                Column('ward', css_class='form-group col-md-4 mb-1'),
                css_class='row'
            ),
        )
