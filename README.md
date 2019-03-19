# GeoData-Django

ISSUES that arose:

1) CSV

    Problem: The csv file was too large for GitHub

    Solution: I added it to my .gitignore file, and used 'git reset --soft HEAD^' and 'git reset HEAD <heatmap/.GeoLite2-City-CSV_20190312/.GeoLite2-City-Blocks-IPv4.csv' to go back to prior commits and remove the file from staging.

2) MINOR HEROKU ERROR

    Problem: I got this error when attempting to deploy to Heroku: [14:42 $ git push heroku setup-heroku:master  error: src refspec setup-heroku does not match any] and remembered that I should have deployed from the master branch. 

    Solution: Updated master branch and switched to master. Committed and pushed to Git, and then to heroku.

3) MAJOR HEROKU ERROR

    Problem: I got this error code when trying to launch the heroku site: code=H10 desc="App crashed", and scrolling up in traceback found: ModuleNotFoundError: No module named 'geodata-django'. I did a project-wide search for 'geodata-django' and found that I had entered it in Procfile as 'web: gunicorn geodata-django.wsgi'. 

    Tried: 

    1. replacing 'geodata-django' with 'GeoData' but got the same message: No module named 'geodata-django'. 

    2. Found https://devcenter.heroku.com/articles/python-pip which addresses how to get heroku to recognize any requirements that are installed locally. Used this command (found on stackoverflow when searching how to make a requirements.txt): pip freeze > requirements.txt . Still the same error (but this step needed to be done). 

    3. Re-ordered apps in settings (put my apps at the bottom of 'installed apps'). 

    4. Tried the instructions from https://help.heroku.com/BWJ7QYTF/why-am-i-seeing-importerror-no-module-named-site-when-deploying-a-python-app 'heroku config'. 

    5. Reviewed heroku set-up: https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true and tried 
    [$ heroku ps:scale web=1] to ensure that at least one instance of the app is running. Got a positive response [Scaling dynos... done, now running web at 1:Free]. 

    6. Restarted heroku 'heroku restart'.

    7. Connected a psql session with my remote database: 20:42 $ heroku pg:psql
    output (abbr.)--> Connecting to gresql-polished-87072
    psql
    blooming-journey-52100::DATABASE=>

    I figured out the problem: the Procfile does need to read 'web: gunicorn geodata.wsgi'. 1st try was the right thing to do, but need to figure out why it didn't work.

    8. I changed it (again), committed and pushed it, and restarted heroku a few times. However heroku continues to call for 'web: gunicorn geodata-django.wsgi' and give the 'no module found named geodata-django' error. Googling this issue only leads to one solution which I've already tried (committing and pushing the correcting to git and 'heroku restart'). 

    9. Tried writing to the Procfile using 'echo "web: python app.py" > Procfile' in command line. This was a cool trick that I'm glad I got to try, but unfortunately same result. https://stackoverflow.com/questions/15790691/procfile-not-found-heroku-python-app

    10. From https://stackoverflow.com/questions/29481506/heroku-procfile-not-working tried $ heroku run bash
    $ cat Procfile
    output --> web: gunicorn geodata-django.wsgi (and no module named yada yada)
    $ web: gunicorn geodata.wsgi
    (Progress! 'no module named geodata' error)
    Repeated above with web: gunicorn GeoData.wsgi (New error! ModuleNotFoundError: No module named 'GeoData.heroku_settings') And that's right, there is no module named that (commented out). Wow, I've been at this for 8 hours minus a 2 hour dinner break. But it's fun because I'm excited to learn more at TransLoc. :)

    12. Un-commented 'heroku_settings.py', pushed to git and to heroku. Got 'Error while running '$ python manage.py collectstatic --noinput'.' Tried adding a css file under 'static'.

    13. Currently getting 'no module named geodata' error. Will set this aside for now to work on the map.

    Solution: It needed to be: web: gunicorn GeoData.wsgi It's working now. 

4.) DATAFRAME VALUE ERROR

    Problem: [print(df)] works, but [return(df)] gets 'ValueError: The truth value of a DataFrame is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().'

    Problem: In load_geodata.py,
    [print(df)] works, but [return(df)] gets 'ValueError: The truth value of a DataFrame is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().'

    Tried: 
        1. df = df[['latitude', 'longitude']]
        df.head() -- no errors
        print(df.head()) -- outputs top 5 rows
          
            latitude  longitude
        0  -35.5016   138.7819
        1   24.4798   118.0819
        2   24.4798   118.0819
        3  -33.4940   143.2104
        4   23.1167   113.2500

        2. print(df.all()) -- outputs 
        latitude     False
        longitude    False
        dtype: bool

        3. print(df.bool()) -- outputs
        ValueError: The truth value of a DataFrame is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

        4. print(df.any()) -- outputs
        latitude     True
        longitude    True
        dtype: bool

    Solution: Scrapping pandas. Goodbye beautiful code! I'll never forget you!

    In memoriam:

    import pandas as pd
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
        df.head() # just top 5 rows

5.) Problem: Need to figure out how to get latitude and longiture data saved    through the Model, so it can then be serialized and written to json. 

    Solution: Used the csv DictReader to isolate lat and long and create model objects.

6.) Problem: 109k+ model objects created during testing that need to be         deleted before creating from full csv file.

    Solution:  I commented out all of the management command and ran this:  LatLong.objects.all().delete()

STEPS to Solve the Code Challenge:

1) Set up Repo on GitHub DONE
	
    Create Django project, pipenv install packages and update settings using Django Quickstart DONE
	Import IPv4 file and set to ignore DONE

    html templates (index, etc) - Need to update access token DONE

    static files: 
        CSS DONE
        JavaScript IN PROGRESS
            (Use REST endpoint in a single-page JavaScript application to display data to user)
	
    url patterns for index page DONE

    model(s), make migrations DONE/may need more fields

    admin class for each model DONE

    views for index page DONE

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

    Write code to return list of coordinates that can be used for JSON  IN PROGRESS

	get latitude and longitude information DONE

3) Research MapBox
    
    Watched 'How to Upload Data in Mapbox Studio' DONE

        Notes fromm video: mapbox.com/studio/datasets; new dataset, upload, drop GeoJSON, JSON or csv file TO DO

        Will need to be JSON from the API to satisfy assignment requirements TO DO

    use Leaflet and Leaflet.heat libraries and others (MapBox GL) to draw geographical data on a map in the browser IN PROGRESS

	Bound in geo bounding box such as MapBox (free tier) DONE

    Make lat and long columns fit mapbox API  RESEARCH

        Read about MapBox GL JS (JS library) https://docs.mapbox.com/mapbox-gl-js/api/ DONE

        Read more about Leaflet.heat DONE

        And read https://docs.mapbox.com/mapbox.js/api/v3.2.0/ REVISIT

        *Note that Leaflet and Mapbox use the reverse order of Longitude, Latitude.

        Choose one: will try MapBox GL JS, because it has a nice tutorial to follow.

            May use:
                heatmap-density
                zoom

        Choose a Style: mapbox://styles/mapbox/satellite-streets-v11 DONE

4) Django REST Framework buildout 

    Define a REST endpoint that returns a list of coordinates within a geographic coordinate bounding box.  Research endpoint requirements. TO DO
       
    url for api in heatmap.urls TO DO

    api app: 
        views TO DO
        serializers DONE
        urls IN PROGRESS

5) Deploy to Heroku DONE

    https://blooming-journey-52100.herokuapp.com/

    Create requirements.txt for dependencies, install heroku using class notes DONE

    Fix deployment crashing problem DONE

BONUS/Opt

	Fine tune data Opt.

    Write tests to verify behavior

	    Test lat/long command function with top 3 lines of CVS file before using on entire file DONE

    Additional tests using tests.py
