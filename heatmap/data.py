import pandas as pd
import requests
import json
from pandas.io.json import json_normalize

df = pd.read_csv(("heatmap/.GeoLite2-City-CSV_20190312/.GeoLite2-City-Blocks-IPv4.csv"), usecols=["latitude", "longitude"])
df = df[['latitude', 'longitude']]
df.head()
