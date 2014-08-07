City on the Set!
============

City on the Set! is a web application which shows the locations in San Francisco that are featured in films, and also, any trivia associated with the location.

Application URL: http://cityontheset.herokuapp.com/

For any questions or enquires, you can use the Help link on the top-right of the application to email me.

---------
Strategy:
---------

In my mind, there were three key pieces of the application that needed to be thought about at a high level.
1. Accessing the filming locations data from the SF Data source
2. Geocoding the locations so that it can be shown on the map
3. Provide an autocomplete capability for searching the list of movies

Accessing the filming locations data from the SF Data source:

I chose availability over the consistency of the filming locations data. For that purpose, I transform the data from SF Data into a schema in the sql database. I initially
chose MySql and then later transitioned it to Postgres because of its ease of management in Heroku.

As for the data model, I broke it down to the following tables. This normalized design helps mitigate duplication of data while also providing the flexibility to easily extend
each of the objects to store additional pieces of information in the future.

    Movies - This will store a unique list of all the movies. This helps especially for the autocomplete feature since it simplifies the query and hence, improves the performance.
      id (PK)
      name
      release_year

    Locations - This stores a list of unique locations, along with their geocoding co-ordinates if available.
      id (PK)
      name
      lat
      lng

    Persons - This stores a unique list of all people - actors, writers and directors
      id (PK)
      name

    Companies - This stores a unique list of all companies - producers and distributors
      id (PK)
      name

    City_Film_Locs - This table brings all of the above information together, and in addition also stores trivia associated with a particular movie and location in the fun_facts column
      id (PK)
      movie_id (FK to Movies)
      location_id (FK to Locations)
      fun_facts
      production_company_id (FK to Companies)
      distributor_id (FK to Companies)
      director_id (FK to Persons)
      writer_id (FK to Persons)
      actor_1_id (FK to Persons)
      actor_2_id (FK to Persons)
      actor_3_id (FK to Persons)

In hindsight, I would probably move the production_company_id, distributor_id, director_id, writer_id, actor_1_id, actor_2_id and actor_3_id columns to the Movies table as opposed to
the City_Film_Locs table since these are attributes of the Movie itself.

Geocoding the locations:

I decided to geocode the location using a separate cron job and store it in the database. Since the lat and lng co-ordinates of a certain location are not bound to change, it made sense
to incur the cost of geocoding a particular location only once. This also helped stay within the Google API quota limits. At this time, the data_dump script is run manually in the Heroku
instance. But, this can easily be scheduled as a rake task in Heroku Scheduler.

Autocomplete:

As for the autocomplete capabiilty, I decided to go with the Jquery autocomplete widget. The widget will make an ajax invocation to the REST API on the Movies object with the partial
string as a query parameter. The response will then be parsed and displayed in the UI.

-----------------
Technology stack:
-----------------
Python:
I have been working with Python for the last 6 months. I am certainly not an expert, but, I do like to embrace the simplicity and readability offered by the language while remaining powerful.

Django:
I have been working with the MVC paradigm for a few years now, and more recently got exposed to Django. I feel one of the highlights of Django is the ability to rapidly develop applications
from the ground up, starting with the data model layer all the way up to the UI. I also enjoy developing using the bundled lightweight web-server, especially due to its hot reload feature.

Django Rest Framework:
I used the Django Rest Framework module to define the REST APIs. The serializers and the generic API views made it easy to process the incoming requests and return the appropriate JSON
responses.

MySQL / Postgres:
My exposure to SQL led me to using MySql as the database backend. But, at deployment time, I realized that Heroku has an add-on to configure and manage Postgres instances more readily than MySql.
So, I migrated my local MySql instance to a Postgres instance, created a db dump and then imported it to Heroku.

Jquery:
I am familiar with Jquery, but, had not used it extensively in my past experience. But, I decided to use this oppourtinity to learn, and leverage the Jquery autocomplete widget for this project.

I chose not to use any front-end MV* frameworks, like Backbone, for this project since I felt that the simplicity of the application did not necessitate such a framework. Even though I would have
liked to explore this option and learn, in this case, the short time line for the challenge led me to reserve it for later.

Google Maps API:
Prior to this project, I had not dealt with the Google APIs. But, kudos to good documentation, this was not too difficult to pick up and use.

Twitter Bootstrap:
I used a free Bootstrap template from Bootswatch to style the application. Given my limited experience with defining custom CSS, I also used the following additional online resources:
  http://css-tricks.com/simple-styles-for-horizontal-rules/
  https://gist.github.com/daz/2168334

Heroku:
I decided to host the application in a Heroku instance since it provided a simple well-documented deployment option for Django applications, along with a Postgres configuration.

PyUnit:
I chose PyUnit as the testing framework to test the REST APIs. The tests are configured to run against the Heroku instance.

-----------
Deployment:
-----------
1. The necessary dependencies are captured in the requirements.txt. Heroku will automatically install these dependencies when creating a new instance.
2. Use the pgbackups addon in Heroku to import the dump file (cityontheset.dump) into a Postgres DB setup in Heroku.
3. The database configuration in Django settings is already configured to use the DATABASE_URL environment variable with the help of the dj_database_url module.
4. Use "git push heroku master" to deploy the app.

-------------
Enhancements:
-------------

The following are some of the product enhancements that I would target given more time:

    1. Using the Google Custom Search API, display thumbnail images for the selected movies and locations
    2. Integrate with the APIs from an online video purchasing / streaming service such as Netflix, Amazon or Google Play to give options to watch the movies