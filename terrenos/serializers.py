from rest_framework import serializers
from .models import Terreno


class TerrenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terreno
        fields = ['id', 'title']