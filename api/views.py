from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from heatmap.models import LatLong
from .serializers import LatLongSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# creates a read only endpoint for all LatLong instances
class LatLongAPIView(generics.ListAPIView):
    queryset = LatLong.objects.all()
    serializer_class = LatLongSerializer

@api_view(['GET'])
def latlong_list(request):
    """
    List all latlong objects.
    """
    if request.method == 'GET':
        latlongs = LatLong.objects.all()
        serializer = LatLongSerializer(latlongs, many=True)
        return JsonResponse(serializer.data, safe=False)
