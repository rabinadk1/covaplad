from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_safe

from . import forms, models

# Create your views here.
# TODO: Send districst when fetching provinces and likewise


def index(request: HttpRequest):
    form = forms.AddressForm(request.POST or None)
    if form.is_valid():
        return HttpResponse("The form was valid!")

    return render(request, "country.html", {"form": form})


@require_safe
def get_provinces(request: HttpRequest, country_id: int):
    provinces = [
        (p.id, str(p))
        for p in models.Province.objects.filter(country_id=country_id).only("name")
    ]
    return JsonResponse({"country_id": country_id, "data": provinces})


@require_safe
def get_districts(request: HttpRequest, province_id: int):
    districts = [
        (d.id, str(d))
        for d in models.District.objects.filter(province_id=province_id).only("name")
    ]
    return JsonResponse({"province_id": province_id, "data": districts})


@require_safe
def get_municipalities(request: HttpRequest, district_id: int):
    municipalities = [
        (m.id, str(m))
        for m in models.Municipality.objects.filter(district_id=district_id).only(
            "name", "is_rural"
        )
    ]
    return JsonResponse({"district_id": district_id, "data": municipalities})


@require_safe
def get_wards(request: HttpRequest, municipality_id: int):
    wards = [
        (w.id, str(w))
        for w in models.Ward.objects.filter(municipality_id=municipality_id).only(
            "number"
        )
    ]
    return JsonResponse({"municipality_id": municipality_id, "data": wards})
