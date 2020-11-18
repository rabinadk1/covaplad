from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import AddressForm

# Create your views here.


def index(request: HttpRequest):
    if request.method == "POST":
        form = AddressForm(request.POST)

        if form.is_valid():
            return HttpResponse("The form was valid!")

    else:
        form = AddressForm()

    return render(request, "country.html", {"form": form})
