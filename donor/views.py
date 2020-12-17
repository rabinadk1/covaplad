from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render

from . import forms
from .models import Donor, TestReport

# Create your views here.


def donor(request: HttpRequest):
    return render(request, "donor.html")


@login_required(redirect_field_name="next")
def donor_registration(request: HttpRequest):
    user = request.user
    if not hasattr(user, "donor"):
        if request.method == "POST":
            form = forms.DonorForm(request.POST, request.FILES)
            if form.is_valid():
                donor = form.save(commit=False)
                donor.user = user
                donor.save()
                # Saving only after donor is saved
                for img in request.FILES.getlist("test_reports"):
                    TestReport(donor=donor, report=img).save()
                return redirect("donor_registration")
        else:
            form = forms.DonorForm()

        return render(request, "donor_registration.html", {"form": form})
    else:
        donor = Donor.objects.get(user=user)
        form = forms.DonorForm(instance=donor)
        for fieldname in form.fields:
            form.fields[fieldname].disabled = True
        has_registered = True
        return render(
            request,
            "donor_registration.html",
            {"form": form, "has_registered": has_registered},
        )
