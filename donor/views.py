from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render

from . import forms

# Create your views here.


@login_required(login_url="login")
def donor_registration(request: HttpRequest):
    form = forms.DonorForm(request.POST or None)

    if form.is_valid():
        return redirect("donor_registration")

    return render(request, "donor_registration.html", {"form": form})
