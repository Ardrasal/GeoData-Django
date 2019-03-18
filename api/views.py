# from django.shortcuts import render

from rest_framework import generics
from heatmap.models import LatLong
from .serializers import LatLongSerializer

# creates a read only endpoint for all LatLong instances
class LatLongAPIView(generics.ListAPIView):
    queryset = LatLong.objects.all()
    serializer_class = LatLongSerializer
