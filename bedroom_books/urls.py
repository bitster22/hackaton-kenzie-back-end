from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BedroomBookView.as_view(), name="list-create-books"),
    path(
        "books/<uuid:book_id>/",
        views.BedroomBookDetailView.as_view(),
        name="retrieve-destroy-books",
    ),
]