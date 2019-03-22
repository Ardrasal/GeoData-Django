# View [Live](https://blooming-journey-52100.herokuapp.com/)

#### Heatmap Code Challenge

It was a pleasure and also quite a challenge to work on this project. Below I have listed the issues that arose in the order that they occurred, what I tried, and how I solved them. Further down is my project steps outline.

##### ISSUES that arose:

1) CSV

    **Problem:** The csv file was too large for GitHub.

    **Solution:** I added it to my .gitignore file, and used `git reset --soft HEAD^` and `git reset HEAD <heatmap/.GeoLite2-City-CSV_20190312/.GeoLite2-City-Blocks-IPv4.csv` to go back to prior commits and remove the file from staging.

2) HEROKU ERROR

    **Problem:** I got an error code when trying to launch the Heroku site: `code=H10 desc="App crashed"`, and scrolling up the traceback I found: `ModuleNotFoundError: No module named 'geodata-django'`. I did a project-wide search for 'geodata-django' and found that I had entered it in the Procfile as `web: gunicorn geodata-django.wsgi`. 

    **Tried:** 

    1. I replaced 'geodata-django' with 'GeoData' but got the same message: `No module named 'geodata-django'`. Ultimately this step was partly the answer.

    2. I reviewed [Heroku set-up](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true) and tried 
    `$ heroku ps:scale web=1` to ensure that at least one instance of the app was running. I got a positive response `Scaling dynos... done, now running web at 1:Free`. 

    3. I restarted Heroku with `heroku restart`.

    4. I connected a psql session with my remote database: `$ heroku pg:psql`
    output (abbr.)--> `Connecting to gresql-polished-87072
    psql
    blooming-journey-52100::DATABASE=>`

    5. I tried writing to the Procfile using `echo "web: python app.py" > Procfile` in the command line. This was a cool trick that I'm glad I got to try, but unfortunately got the same result. (https://stackoverflow.com/questions/15790691/procfile-not-found-heroku-python-app)

    6. From (https://stackoverflow.com/questions/29481506/heroku-procfile-not-working) I tried `$ heroku run bash
    $ cat Procfile`
    output --> `web: gunicorn geodata-django.wsgi` and `no module named geodata-django`.
    I entered:
    `$ web: gunicorn geodata.wsgi`
    (Progress! I got a `no module named geodata` error.) I repeated these steps with `web: gunicorn GeoData.wsgi` (New error! `ModuleNotFoundError: No module named 'GeoData.heroku_settings`) And that's right, there was no module named that at the time (it was temporarily commented out).

    7. I un-commented heroku_settings.py', pushed to git and to Heroku. I got an error while running `$ python manage.py collectstatic --noinput`. I tried adding a css file under 'static/'.

    **Solution**: It needed to be: `web: gunicorn GeoData.wsgi`, but I had neglected to push to Heroku, and fix a few other things such as un-commenting heroku_settings.py and adding my requirements.txt.

    **Lessons Learned:** 
    
    I should make all apps, projects, and files lower case to reduce the chance of this type of error. I am now well-versed in the Heroku deployment. In the past I had done no more than one deployment per project; I did not have experience with doing it frequently. I was following a guide and didn't have the process memorized. But I do now!

3) DATAFRAME VALUE ERROR

    **Problem:**  In load_geodata.py, `print(df)` works, but `return(df)` gets a `ValueError: The truth value of a DataFrame is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().`

    **Tried:** 

        1. `df = df[['latitude', 'longitude']]
        df.head()` -- no errors
        `print(df.head())` -- outputs top 5 rows
          
            latitude  longitude
        0  -35.5016   138.7819
        1   24.4798   118.0819
        2   24.4798   118.0819
        3  -33.4940   143.2104
        4   23.1167   113.2500

        2. `print(df.all())` -- outputs 
        latitude     False
        longitude    False
        dtype: bool

        3. `print(df.bool())` -- outputs
        `ValueError: The truth value of a DataFrame is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().`

        4. `print(df.any())` -- outputs
        latitude     True
        longitude    True
        dtype: bool

    **Solution:** 
    
    I consulted with Clinton from Momentum, who thought that pandas would be problematic for the future steps in this challenge. He suggested I use the simpler csv Reader that I had previously rejected. Specifically, the DictReader. So I scrapped pandas. I spent many hours working with pandas in this project. Goodbye beautiful code! I'll never forget you!

    In memoriam:

    `import pandas as pd
    # import io

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
        df = df[['latitude', 'longitude']]
        df.head() # just top 5 rows`

4) SAVE LAT AND LONGS FROM CSV

    **Problem:** 

    I needed to figure out how to get the latitude and longitude data saved through the LatLong Model, so it could then be serialized and written to a json (or geojson) api endpoint. 

    **Solution:** 
    
    I used the csv DictReader to isolate lat and long, and create model objects. Then used the ModelSerializer class to manipulate the serialization, and send it through the ListAPIView to return the GeoJSON data in the api endpoint.

5) DELETE LARGE NUMBER OF TEST OBJECTS

    **Problem:** 

    109k+ model objects were created during testing, that needed to be deleted before creating from the full csv file of 3 million + objects.

    **Solution:**  
    
    I commented out the code in the handle management command function, and instead ran `LatLong.objects.all().delete()`.

6) VALIDATION ERROR

    **Problem:**   

    When running my management command to pull out latitudes and longitudes from the csv and create objects, I got the following error:

    `.../python3.7/site-packages/django/db/models/fields/__init__.py", line 1559, in to_python
    params={'value': value}, django.core.exceptions.ValidationError: ["'' value must be a decimal number."]`

    **Tried:** 
    
    I looked through the cvs, and saw that some of the lat/long values were whole numbers. I reasearched to see if that could throw the error, and it didn't look like it should, because the decimal field of the LatLong model turns whole numbers into numbers with zeros after the decimal point. I revisited my choice to choose the decimal field over the float field. I decided that decimal field should be fine.

    **Solution:** 
    
    To get around the error, I added this to my function:

    `try:
        LatLong.objects.create(latitude=row['latitude'], longitude=row['longitude'])
    except ValidationError:
        pass`

7) ACCIDENTAL LARGE FILE PUSH

    **Problem:** 

    I accidentally pushed my data.dump file, created to attempt to populate the database on Heroku with the database created locally, onto Git. 
    
    **Tried:**
    
    I deleted the file from the project and from Git, but Git became frozen in a loop with the file stuck in limbo somehow.

    **Solution:** 

    I followed the steps in the link below:
    
    (https://stackoverflow.com/questions/19573031/cant-push-to-github-because-of-large-file-which-i-already-deleted)

8) SERIALIZE MODEL OBJECTS INTO GEOJSON

    **Problem:**

    Even though hardcoded test points written in GeoJSON format rendered on the heatmap layer, and even though I wrote a serializer that rendered identical looking GeoJSON, the console showed an error that said it was not valid GeoJSON.

    **Solution:**

    I researched, tweaked, and repeatedly tested the map.on('load', function() in my map.js, the serializer, and the view (and the type of view), and ultimately what worked was the def list method added to the ListAPIView.

##### STEPS:

1) Set up Project

    Create:

    - repo on GitHub

    - Django project 

    - html templates

    - static files: 
        CSS
        JavaScript (finish at the end)

	- urls

    - model(s), make migrations

    - admin class for each model

    - views for index page

2) Research how to access csv file in Django
    
    Write the python script

    Test in Python shell

    Create a management command to load csv file

    Test parsing lat/long data from sample (top three lines) of csv

    Parse data from entire IPv4 file
	
        Decide between these two methods (initially chose pandas but later switched to csv Reader)

		    csv module: (https://docs.python.org/3/library/csv.html) 

	        Parse specific columns from csv file 
		    (https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module)

    Write code to return list of coordinates that can be used for JSON

    Create model objects (25 minutes to load!)

3) Research MapBox

    Must be JSON from the API to satisfy assignment requirements

    Research using MapBox, MapBox gl JS, Leaflet, and Leaflet-heat to draw geographical data on a map in the browser

    Convert JSON to GeoJSON in this format:

            `{
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [125.6, 10.1]
            }
            }`

    Coordinates in this order: long, lat

	Bind in geo bounding box using MapBox

4) Django REST Framework buildout 

    Research endpoint requirements for heatmap
    
    Define a REST endpoint that returns a list of coordinates within a geographic coordinate bounding box 
       
    url for api in heatmap.urls 

    api app: 

        views 

        serializers 

        (https://www.django-rest-framework.org/api-guide/fields/#decimalfield)

        urls 

5) Deploy to Heroku 

    Create requirements.txt for dependencies
    
    install Heroku

    (https://blooming-journey-52100.herokuapp.com/)
    
Finishing Steps: 

        1. Follow steps from (https://jaketrent.com/post/django-loaddata-heroku/) to dump data from database onto Heroku (bypasses Git in a way). Remove .json file from project.

        2. Serialize model objects to output GeoJSON; store them in an api endpoint

            serializers.py
            api/views.py
            api/urls.py

        3. Push to Heroku

        4. Add api endpoint to map.addSource; check that it adds points on heat layer of map.

        5. Check that requirements.txt is up to date

        6. Push to git

        7. Push to heroku, limiting queryset to 1000 so the server connection will not time out. Continue to raise queryset and test

        8. Submit


