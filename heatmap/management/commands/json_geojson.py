# Called with 'python manage.py json_geojson.py'
# Used this answer to create function that turns json into geojson. 
# https://gis.stackexchange.com/questions/180806/help-with-manipulating-json-to-geojson

from django.core.management.base import BaseCommand
import json
# limit print output for test
import reprlib

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        r = reprlib.Repr()
        r.maxlist = 4
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [125.6, 10.1]
            }
        }

        json.dumps(feature)
# First tested 'heatmap/test.json'.
        with open('https://blooming-journey-52100.herokuapp.com/api/', 'w') as stream:
            json.dump(feature, stream, indent=2)
        print(r.rep(feature))

# outputs {'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [125.6, 10.1]}}
