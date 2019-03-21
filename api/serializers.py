# from django.core.serializers import DjangoJSONEncoder
from heatmap.models import LatLong
from rest_framework import serializers


class LatLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatLong
        fields = ('latitude', 'longitude')

    def to_representation(self, instance):
        # print("to_representation method")
        data = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [float(instance.longitude), float(instance.latitude)]}}
        print(data["geometry"])
        return data
