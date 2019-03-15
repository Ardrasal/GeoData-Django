# GeoData-Django

Issues:

1) The csv file was too large for github, so I added it to my .gitignore file, and used 'git reset --soft HEAD^' and 'git reset HEAD <heatmap/.GeoLite2-City-CSV_20190312/.GeoLite2-City-Blocks-IPv4.csv' to go back to prior commits and remove the file from staging.

Steps:

Set up Repo on GitHub DONE
	Create Django REST framework project, pipenv install packages and update settings using Django Quickstart DONE
	import IPv4 file and set to ignore DONE

Research how to access csv file in Django DONE
Write the python script DONE
Make it work in Python shell DONE

Management command to load csv file DONE

Research models for Latitude and Longitude - DONE/MAY NEED MORE FIELDS

Test if can parse lat/long data from limit of 50 numbers DONE
	make lat columns = x and long column = y (make fit mapbox API) RESEARCH

Parse data from IPv4 file DONE
	parse data
		csv module: https://docs.python.org/3/library/csv.html NO

	research how to parse specific columns from csv file YES
		https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module

import pandas as pd DONE
df = pd.read_csv(csv_file) DONE with lat/long
saved_column = df.column_name #you can also use df['column_name'] RESEARCH

	get latitude and longitude information DONE

Define a REST endpoint that returns a list of coordinates within a geographic coordinate bounding box (may need to fine tune resolution of data to improve performance) 
	research REST endpoint
	write code to return list of coordinates
		use Leaflet and Leaflet.heat libraries and others to draw geographical data on a map in the browser

	bound in geo bounding box such as MapBox (free tier)
	Opt: fine tune data

Use REST endpoint in a single-page JavaScript application to display data to user
	code REST endpoint in JS (user can zoom into map and see ipv4 data)

Deploy to Heroku

BONUS

Write tests to verify behavior
	review how to write tests (assert function)
