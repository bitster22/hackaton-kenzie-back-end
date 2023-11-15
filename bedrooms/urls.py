from django.urls import path
from . import views

urlpatterns = [
    path("bedrooms/", views.BedroomView.as_view(), name="list-create-bed"),
    path(
        "bedrooms/<uuid:bed_id>/",
        views.BedroomDetailView.as_view(),
        name="update-retrieve-destroy-beds",
    ),
]