from django.urls import path
from . import views

urlpatterns = [
    path("sales/", views.SaleView.as_view(), name="list-create-sale"),
    path(
        "sales/<uuid:sale_id>/",
        views.SaleDetailView.as_view(),
        name="update-retrieve-destroy-sale",
    ),
]