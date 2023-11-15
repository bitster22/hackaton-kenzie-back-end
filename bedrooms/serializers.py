from rest_framework import serializers
from .models import Bedroom


class BedroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bedroom
        fields = "__all__"