# from rest_framework import serializers
from django.core.serializers import serialize
from heatmap.models import LatLong

# for JSON API endpoint
# class LatLongSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LatLong
#         fields = ('latitude', 'longitude')

# for geojson endpoint
serialize('geojson', LatLong.objects.all(), geometry_field='point')
