from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("country/<int:country_id>/", views.get_provinces, name="get_provinces"),
    path("province/<int:province_id>/", views.get_districts, name="get_districts"),
    path(
        "district/<int:district_id>/",
        views.get_municipalities,
        name="get_municipalities",
    ),
    path("municipality/<int:municipality_id>/", views.get_wards, name="get_wards"),
]
