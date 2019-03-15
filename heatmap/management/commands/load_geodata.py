# I used this tutorial to remind me how to make a management command to load the parsed csv data. https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html

# This will be called with python manage.py load_geodata

from django.core.management.base import BaseCommand

# To extract the lat/long data, I used information from https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module/41004218#41004218 specifically from this answer currently with a score of 13:

# With pandas you can use read_csv with usecols parameter:

import pandas as pd
import io

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # The truncated_data test below works.
        # truncated_data = '''
        # network,geoname_id,registered_country_geoname_id,represented_country_geoname_id,is_anonymous_proxy,is_satellite_provider,postal_code,latitude,longitude,accuracy_radius
        # 1.0.0.0/24,2070667,2077456,,0,0,5214,-35.5016,138.7819,100
        # 1.0.1.0/24,1811017,1814991,,0,0,,24.4798,118.0819,50
        # '''
        # df = pd.read_csv(io.StringIO(truncated_data), usecols=["latitude", "longitude"])
        # Now will try to parse from the entire csv file.
        df = pd.read_csv(("heatmap/.GeoLite2-City-CSV_20190312/.GeoLite2-City-Blocks-IPv4.csv"), usecols=["latitude", "longitude"])
        # saved_lat = df.latitude
        print(df)
