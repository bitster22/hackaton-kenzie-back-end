from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveDestroyAPIView,
)
from .models import BedroomBook
from .serializers import BedroomBookSerializer


class BedroomBookView(ListCreateAPIView):
    queryset = BedroomBook.objects.all()
    serializer_class = BedroomBookSerializer


class BedroomBookDetailView(RetrieveDestroyAPIView):
    queryset = BedroomBook.objects.all()
    serializer_class = BedroomBookSerializer
    lookup_url_kwarg = "book_id"
