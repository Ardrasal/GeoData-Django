# I used this tutorial to remind me how to make a management command to load the parsed csv data: https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html

# Called with 'python manage.py load_geodata'

from django.core.management.base import BaseCommand
import csv
from heatmap.models import LatLong

import pandas as pd

class Command(BaseCommand):
    # df = pd.read_csv(("heatmap/.GeoLite2-City-CSV_20190312/.GeoLite2-City-Blocks-IPv4.csv"), usecols=["latitude", "longitude"])
    
    with open('heatmap/.GeoLite2-City-CSV_20190312/.GeoLite2-City-Blocks-IPv4.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        
        next(csvreader)
        for row in df:
            # breakpoint()

    with open('heatmap/testdata.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        next(csvreader)
            for row in reader:
            #  clean all this up and add specific columns
            LatLong.objects.create(latitude=row['latitude'], longitude=row['longitude'])
