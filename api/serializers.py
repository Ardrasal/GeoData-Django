from rest_framework import serializers
from heatmap.models import LatLong

# for JSON API endpoint
class LatLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatLong
        fields = ('latitude', 'longitude')
