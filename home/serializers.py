from rest_framework import serializers
from .models import Maktablar

class MaktablarSerializer(serializers.ModelSerializer):\

    full_link = serializers.SerializerMethodField()

    class Meta:
        model = Maktablar
        fields = '__all__'


    def get_full_link(self, obj):
        return f"https://school.utu-ranch.uz/{obj.slug}"
