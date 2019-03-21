from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework import generics
from heatmap.models import LatLong
# from .serializers import LatLongSerializer
from django.http import JsonResponse
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

class LatLongAPIView(generics.ListAPIView):
    """
    Creates a read only endpoint for all LatLong instances.
    """
    queryset = LatLong.objects.all()
    serializer_class = LatLongSerializer

@api_view(['GET'])
def latlong_list(request):
    """
    Lists all latlong objects.
    """
    if request.method == 'GET':
        latlongs = LatLong.objects.all()
        serializer = LatLongSerializer(latlongs, many=True)
        return JsonResponse(serializer.data, safe=False)
