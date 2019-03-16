from rest_framework import serializers
from heatmap.models import LatLong

class LatLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatLong
        fields = ('latitude', 'longitude')
