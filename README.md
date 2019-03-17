# GeoData-Django

ISSUES that arose:

1) CSV

The csv file was too large for GitHub, so I added it to my .gitignore file, and used 'git reset --soft HEAD^' and 'git reset HEAD <heatmap/.GeoLite2-City-CSV_20190312/.GeoLite2-City-Blocks-IPv4.csv' to go back to prior commits and remove the file from staging.

2) MINOR HEROKU ERROR

I got this error when attempting to deploy to Heroku [14:42 $ git push heroku setup-heroku:master
error: src refspec setup-heroku does not match any] and remembered that I'm supposed to deploy from the master branch. Updated master branch and switched to master--didn't work.
Then tried adding a file (touch notes), commiting, and trying again (based on several answers on stackoverflow)--also didn't work.
Then tried $ git push heroku HEAD:master 
--it worked!

3) MAJOR HEROKU ERROR

I got this error code when trying to launch the heroku site: code=H10 desc="App crashed", and scrolling up in traceback found: ModuleNotFoundError: No module named 'geodata-django'. I did a project-wide search for 'geodata-django' and found that I had entered it in Procfile as 'web: gunicorn geodata-django.wsgi'. 

Tried the following: 

1. replacing 'geodata-django' with 'GeoData' but got the same message: No module named 'geodata-django'. 

2. Searched online and found https://devcenter.heroku.com/articles/python-pip which addresses how to get heroku to recognize any requirements that are installed locally. Used this command (found on stackoverflow when searching how to make a requirements.txt): pip freeze > requirements.txt . Still the same error (but this step needed to be done anyway). 

3. Re-ordered apps in settings (put my apps at the bottom of 'installed apps'). 

4. Tried the instructions from https://help.heroku.com/BWJ7QYTF/why-am-i-seeing-importerror-no-module-named-site-when-deploying-a-python-app 'heroku config'. 

5. Reviewed heroku set-up: https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true and tried 
[$ heroku ps:scale web=1] to ensure that at least one instance of the app is running. Got a positive response [Scaling dynos... done, now running web at 1:Free]. 

6. Tried restarting heroku. 

7. Tried connecting a psql session with my remote database: 20:42 $ heroku pg:psql
output--> Connecting to gresql-polished-87072
psql (11.1, server 11.2 (Ubuntu 11.2-1.pgdg16.04+1))
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
Type "help" for help.
blooming-journey-52100::DATABASE=>

I figured out the problem: the Procfile needs to read 'web: gunicorn geodata.wsgi'. 

8. I changed it (again), committed and pushed it, and restarted heroku a few times. However heroku continues to call for 'web: gunicorn geodata-django.wsgi' and give the 'no module found named geodata-django' error. Googling this issue only leads to one solution which I've already tried (committing and pushing the correcting to git and 'heroku restart'). 

9. Tried writing to the Procfile using 'echo "web: python app.py" > Procfile' in command line. This was a cool trick that I'm glad I got to try, but unfortunately same result. https://stackoverflow.com/questions/15790691/procfile-not-found-heroku-python-app

10. From https://stackoverflow.com/questions/29481506/heroku-procfile-not-working tried $ heroku run bash
$ cat Procfile
output --> web: gunicorn geodata-django.wsgi (and no module named yada yada)
$ web: gunicorn geodata.wsgi
(Progress! 'no module named geodata' error.)
Repeated above with web: gunicorn GeoData.wsgi (New error! ModuleNotFoundError: No module named 'GeoData.heroku_settings' And that's right, there is no module named that (commented out). Wow, I've been at this for 8 hours minus a 2 hour dinner break. But it's fun because I'm excited to learn more at TransLoc!)

12. Uncommented 'heroku_settings.py', pushed to git and to heroku. Got 'Error while running '$ python manage.py collectstatic --noinput'.' Tried adding a css file under 'staticfiles'.

13. Currently getting 'no module named geodata' error. Will set this aside for now to work on the map.

4.) DataFrame value error

    [print(df)] works, but [return(df)] gets 'ValueError: The truth value of a DataFrame is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().'


STEPS to Solve the Code Challenge:

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

        Read about MapBox GL JS (JS library) https://docs.mapbox.com/mapbox-gl-js/api/ DONE

        Read more about Leaflet.heat

        And read https://docs.mapbox.com/mapbox.js/api/v3.2.0/

        Note that Leaflet and Mapbox use the reverse order of Longitude, Latitude.

        Choose one: will try MapBox GL JS, because it has a nice tutorial to follow.

            May use:
                heatmap-density
                zoom

        Choose a Style: mapbox://styles/mapbox/satellite-streets-v11
            $ curl "https://api.mapbox.com/styles/v1/ardrasa1?access_token=YOUR_MAPBOX_ACCESS_TOKEN
This endpoint requires a token with styles:list scope.
"
        
    Create GeoJSON file https://pypi.org/project/geojson/
        In my Quizzer group project, I used a dumpdata command to create a json file from data quizzes I had created in my database. Then had my teammates drop their databases and run command so they would have identical sample data: [$ psql][DROP DATABASE flashcards][createdb flashcards][control-D to exit][$ ./manage.py loaddata sample_data.json]
        Researched and found that dumpdata command only creates JSON, not GeoJSON.
        
        It can be done with GeoPandas -> GeoJSON

4) Finish Django REST Framework buildout
    
    html templates (index, etc) STARTED - Need to update access token

    static files STARTED

    url patterns for index page DONE

    model(s), make migrations DONE/may need more fields

    admin class for each model DONE

    views DONE

    api app: views, serializers, urls IN PROGRESS

5) Define a REST endpoint that returns a list of coordinates within a geographic coordinate bounding box (may need to fine tune resolution of data to improve performance) 
	
    Research REST endpoint

	Write code to return list of coordinates

		use Leaflet and Leaflet.heat libraries and others to draw geographical data on a map in the browser

	Bound in geo bounding box such as MapBox (free tier)

	Fine tune data

6) Use REST endpoint in a single-page JavaScript application to display data to user
	
    Code REST endpoint in JS (user can zoom into map and see ipv4 data)

7) Deploy to Heroku

    Checked that Heroku was installed, and upgraded from 7.18.10 to 7.22.7 DONE


BONUS

Write tests to verify behavior

	review how to write tests (assert function)
