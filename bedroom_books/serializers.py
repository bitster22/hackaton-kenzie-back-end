from rest_framework import serializers
from .models import BedroomBook


class BedroomBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BedroomBook
        fields = "__all__"