from rest_framework import serializers
from .models import Hero
# Create your serializers.py here.

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')