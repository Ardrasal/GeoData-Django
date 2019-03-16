# GeoData-Django

Issues:

1) The csv file was too large for github, so I added it to my .gitignore file, and used 'git reset --soft HEAD^' and 'git reset HEAD <heatmap/.GeoLite2-City-CSV_20190312/.GeoLite2-City-Blocks-IPv4.csv' to go back to prior commits and remove the file from staging.

Steps:

1) Set up Repo on GitHub DONE
	
    Create Django REST framework project, pipenv install packages and update settings using Django Quickstart DONE
	Import IPv4 file and set to ignore DONE

2) Research how to access csv file in Django DONE
    
    Write the python script DONE
    Make it work in Python shell DONE

    Management command to load csv file DONE

    Test if can parse lat/long data from top three lines of csv DONE

    Parse data from IPv4 file DONE
	
		csv module: https://docs.python.org/3/library/csv.html NO

	    Parse specific columns from csv file YES
		https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module

    import pandas as pd DONE
    df = pd.read_csv(csv_file) DONE with lat/long
    saved_column = df.column_name #you can also use df['column_name'] RESEARCH

	get latitude and longitude information DONE

3) Research MapBox
    
    Watched 'How to Upload Data in Mapbox Studio' DONE
        Notes from video: mapbox.com/studio/datasets; new dataset, upload, drop GeoJSON, JSON or csv file
    Need GeoJSON, JSON, or csv file
        (csv will be too large)
    Research GeoJSON
        Read Using GeoJSON with Leaflet https://leafletjs.com/examples/geojson/ DONE
        Using GeoJSON with a Bounding Box https://tools.ietf.org/html/rfc7946#section-5
    Make lat and long columns fit mapbox API  RESEARCH
        Read about MapBox GL JS (JS library) https://docs.mapbox.com/mapbox-gl-js/api/
        Read more about Leaflet.heat
        And read https://docs.mapbox.com/mapbox.js/api/v3.2.0/
        Choose one: 
    Create GeoJSON file https://pypi.org/project/geojson/

4) Finish Django REST Framework buildout
    
    html templates (index, etc) STARTED - Need to update access token
    static files STARTED
    url patterns for index page DONE
    model(s), make migrations DONE/may need more fields
    admin class for each model DONE
    views DONE
    api app: views, serializers, urls

5) Define a REST endpoint that returns a list of coordinates within a geographic coordinate bounding box (may need to fine tune resolution of data to improve performance) 
	
    Research REST endpoint
	Write code to return list of coordinates
		use Leaflet and Leaflet.heat libraries and others to draw geographical data on a map in the browser

	Bound in geo bounding box such as MapBox (free tier)
	Opt: fine tune data

6) Use REST endpoint in a single-page JavaScript application to display data to user
	
    Code REST endpoint in JS (user can zoom into map and see ipv4 data)

7) Deploy to Heroku

BONUS

Write tests to verify behavior
	review how to write tests (assert function)
