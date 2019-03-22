from rest_framework.response import Response
from rest_framework import generics
from heatmap.models import LatLong
from .serializers import LatLongSerializer


class LatLongAPIView(generics.ListAPIView):
    """
    Creates a read only endpoint for all LatLong instances.
    """
    queryset = LatLong.objects.all()[:1000]
    serializer_class = LatLongSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = LatLongSerializer(queryset, many=True)
        data = {"type": "FeatureCollection", "features": serializer.data}
        return Response(data)
