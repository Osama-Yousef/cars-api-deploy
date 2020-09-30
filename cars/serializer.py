from rest_framework import serializers

from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'body', 'created_at')
        model = Car