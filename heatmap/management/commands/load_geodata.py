# I used this tutorial to remind me how to make a management command to load the parsed csv data: https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html

# Called with 'python manage.py load_geodata'

from django.core.management.base import BaseCommand

# To extract the lat/long data, I used this answer "With pandas you can use read_csv with usecols parameter" from https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module/41004218#41004218

import pandas as pd
# import io (used in truncated-data test)
import geojson

# https://docs.djangoproject.com/en/2.1/howto/custom-management-commands/
class Command(BaseCommand):
    help = 'Pulls latitude and longitude data from csv file and converts it into a GeoJSON file'
    # https://docs.python.org/3/library/argparse.html#module-argparse

    def add_aruments(self, parser):
        parser.add_argument('geojson', nargs='+')

    def handle(self, *args, **kwargs):
        # Truncated_data test:
        # truncated_data = '''
        # network,geoname_id,registered_country_geoname_id,represented_country_geoname_id,is_anonymous_proxy,is_satellite_provider,postal_code,latitude,longitude,accuracy_radius
        # 1.0.0.0/24,2070667,2077456,,0,0,5214,-35.5016,138.7819,100
        # 1.0.1.0/24,1811017,1814991,,0,0,,24.4798,118.0819,50
        # '''
        # df = pd.read_csv(io.StringIO(truncated_data), usecols=["latitude", "longitude"])
        # Parses from entire csv file:
        df = pd.read_csv(("heatmap/.GeoLite2-City-CSV_20190312/.GeoLite2-City-Blocks-IPv4.csv"), usecols=["latitude", "longitude"])
        # lat = df.latitude
        # long = df.longitude
        # return(df)
        print(df)


# Found the following solution from https://gis.stackexchange.com/questions/220997/pandas-to-geojson-multiples-points-features-with-python

def data2geojson(df):
    features = []
    insert_features = lambda X: features.append(
        geojson.Feature(geometry=geojson.Point((X["longitude"], X["latitude"]))))
    df.apply(insert_features, axis=1)
    with open('heatmap.geojson', 'w', encoding='utf8') as fp:
        geojson.dump(geojson.FeatureCollection(features), fp, sort_keys=True, ensure_ascii=False)

col = ['latitude', 'longitude']
data = [[-29.9953, -70.5867],
        [-30.1217, -70.4933],
        [-30.0953, -70.5008]]

df = pd.DataFrame(data, columns=col)

data2geojson(df)
# print(data2geojson(df))

# Or can try this tutorial: https://medium.com/@djosephhenri/mapping-detroits-high-poverty-areas-and-their-access-to-public-transit-using-geopandas-mapbox-72fa21a0bd79