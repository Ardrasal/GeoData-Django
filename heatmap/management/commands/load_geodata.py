# I used this tutorial to remind me how to make a management command to load the parsed csv data: https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html

# Adapted code from https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module

# Called with 'python manage.py load_geodata'

from django.core.management.base import BaseCommand
import csv
from heatmap.models import LatLong
from django.core.exceptions import ValidationError


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('heatmap/.GeoLite2-City-CSV_20190312/.GeoLite2-City-Blocks-IPv4.csv') as csvfile:

            # get number of columns
            len(csvfile.readline().split(','))
            csvfile.seek(0)

            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    LatLong.objects.create(latitude=row['latitude'], longitude=row['longitude'])
                except ValidationError:
                    pass

        # LatLong.objects.all().delete()
