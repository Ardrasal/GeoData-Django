# from rest_framework import serializers
from django.core.serializers import serialize
from heatmap.models import LatLong

class LatLongSerializer(request):
    # for geojson endpoint
    # Used example from https://briancaffey.github.io/2018/02/19/leaflet-maps-with-django.html
    def all_latlongs():
        """
        Main view for latlongs. request.GET parameters are used to filter latlongs.
        """
    latlongs = LatLong.objects.all()
    paramDict = request.GET

    latlongs = filter_latlongs(latlongs, paramDict)

    # This takes the first latlong query and reformats the data so it can be read
    # by the map script on the frontend. 
    # Needs to look like this.
    # {
#     "type": "Feature",
#     "geometry": {
#       "type": "Point",
#       "coordinates": [-78.839185, 35.773980]
#     }
# Need to make sure lat long is in order that library uses.
    map_latlongs = [{"type": "Feature", "geometry": {"type": "Point", "coordinates": [float(latlong.latitude), float(latlong.longitude)], 'url':latlong.get_absolute_url()} for latlong in latlongs}]
    context = {
        'latlongs': latlongs,
        # Here, we apply `json.dumps`, `escapejs` and `marksafe` for security 
        # and proper formatting
        'map_latlongs': mark_safe(escapejs(json.dumps(map_latlongs)))
    }
    return render(request, 'latlongs/index.html', context)

        # This one uses geodjango--scrapping probably.
        # serialize = serialize('geojson', LatLong.objects.all(), geometry_field='point')
        # return geojson(serialize)

# (serializers.ModelSerializer):
#     class Meta:
#         model = LatLong
#         fields = ('latitude', 'longitude')
