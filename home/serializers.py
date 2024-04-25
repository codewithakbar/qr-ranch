from rest_framework import serializers
from .models import Maktablar

class MaktablarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maktablar
        fields = '__all__'
