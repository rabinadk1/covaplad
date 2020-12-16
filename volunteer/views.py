from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from . import forms, models

# Create your views here.


def index(request):
    return HttpResponse("You're at the volunteers url.")


@login_required
def volunteer_registration(request: HttpResponse):
    user = request.user
    if not hasattr(user, "volunteer"):
        form = forms.VolunteerForm(request.POST or None)
        if form.is_valid():
            volunteer = form.save(commit=False)
            volunteer.user = user
            volunteer.save()
            return redirect("volunteer_registration")
        return render(request, "volunteer_registration.html", {"form": form})
    else:
        volunteer = models.Volunteer.objects.get(user=user)
        form = forms.VolunteerForm(instance=volunteer)
        for fieldname in form.fields:
            form.fields[fieldname].disabled = True
        has_registered = True
        return render(
            request,
            "volunteer_registration.html",
            {"form": form, "has_registered": has_registered},
        )
