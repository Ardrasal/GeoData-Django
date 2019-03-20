# Called with 'python manage.py json_geojson.py'
# Used this answer to create function that turns json into geojson. 
# https://gis.stackexchange.com/questions/180806/help-with-manipulating-json-to-geojson

from django.core.management.base import BaseCommand
import json

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [125.6, 10.1]
            }
        }

        json.dumps(feature)

        with open('heatmap/test.json', 'w') as stream:
            json.dump(feature, stream, indent=2)
        print(feature)

# outputs {'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [125.6, 10.1]}}
