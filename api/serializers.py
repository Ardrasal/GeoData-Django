# from rest_framework import serializers
from django.core.serializers import serialize
from heatmap.models import LatLong


class LatLongSerializer(request):
    # for geojson endpoint
    def geojson():
        serialize = serialize('geojson', LatLong.objects.all(), geometry_field='point')
        return geojson(serialize)

# (serializers.ModelSerializer):
#     class Meta:
#         model = LatLong
#         fields = ('latitude', 'longitude')
