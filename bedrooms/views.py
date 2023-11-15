from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Bedroom
from .serializers import BedroomSerializer


class BedroomView(ListCreateAPIView):
    queryset = Bedroom.objects.all()
    serializer_class = BedroomSerializer


class BedroomDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Bedroom.objects.all()
    serializer_class = BedroomSerializer
    lookup_url_kwarg = "bed_id"
