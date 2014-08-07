__author__ = 'kalyang'

import os, sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if PROJECT_ROOT not in sys.path:
    sys.path += [PROJECT_ROOT]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cityontheset.settings")

from cityontheset.src.models import Movie,Location,Person,Company,CityFilmLoc
import urllib2, json, re
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist

SF_DATA_URL = "http://data.sfgov.org/resource/yitu-d5am.json"
BASE_GEOCODE_URL = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&components=locality:SF|administrative_area:CA|country:US"

def geocode(address):
    # if there is an exact address within parantheses, use that. else use the address string as is
    exactAddress = re.findall(r'\((.*?)\)', address)
    if not exactAddress:
        exactAddress.append(address)

    # urlencode the address string and fire the geocode request
    geocode_url = BASE_GEOCODE_URL % urllib2.quote((exactAddress[0]).encode("utf8"))
    response = urllib2.urlopen(geocode_url)
    data = json.loads(response.read())

    # proceed only if the status is OK or ZERO_RESULTS
    if (data['status'] != "OK" and data['status'] != "ZERO_RESULTS"):
        return None, None

    # if we fired the request with address inside the parantheses, but, it did not yield any results,
    # re-issue the request with the complete string as a fallback option
    if(len(data['results']) == 0 and exactAddress != address):
        exactAddress[0] = address
        geocode_url = BASE_GEOCODE_URL % urllib2.quote((exactAddress[0]).encode("utf8"))
        response = urllib2.urlopen(geocode_url)
        data = json.loads(response.read())

    print "Done geocoding addr : " + geocode_url
    return data['results'][0]['geometry']['location']['lat'], data['results'][0]['geometry']['location']['lng']

def processData():
    response = urllib2.urlopen(SF_DATA_URL)
    raw_data = response.read().decode('utf-8')
    data = json.loads(raw_data)

    for idx,elem in enumerate(data):
        try:
            director = None
            writer = None
            production_company = None
            distributor = None
            actor_1 = None
            actor_2 = None
            actor_3 = None

            with transaction.atomic():
                print "Processing element # %s" % idx

                if elem.get('title'):
                    try:
                        movie = Movie.objects.get(name=elem.get('title'))
                    except ObjectDoesNotExist:
                        movie = Movie(name=elem.get('title'), release_year=elem.get('release_year'))
                        movie.save()
                else:
                    raise Exception( "Required information: Title not present. Skipping element.")

                if elem.get('locations'):
                    try:
                        location = Location.objects.get(name=elem.get('locations'))

                        if not location.lat or not location.lng:
                            location.lat, location.lng = geocode(elem.get('locations'))
                            location.save()

                    except ObjectDoesNotExist:
                        location = Location(name=elem.get('locations'))
                        location.lat, location.lng = geocode(elem.get('locations'))
                        location.save()
                else:
                    raise Exception("Required information: Location not present. Skipping element.")

                if elem.get('production_company'):
                    try:
                        production_company = Company.objects.get(name=elem.get('production_company'))
                    except ObjectDoesNotExist:
                        production_company = Company(name=elem.get('production_company'))
                        production_company.save()
                if elem.get('distributor'):
                    try:
                        distributor = Company.objects.get(name=elem.get('distributor'))
                    except ObjectDoesNotExist:
                        distributor = Company(name=elem.get('distributor'))
                        distributor.save()
                if elem.get('writer'):
                    try:
                        writer = Person.objects.get(name=elem.get('writer'))
                    except ObjectDoesNotExist:
                        writer = Person(name=elem.get('writer'))
                        writer.save()
                if elem.get('director'):
                    try:
                        director = Person.objects.get(name=elem.get('director'))
                    except ObjectDoesNotExist:
                        director = Person(name=elem.get('director'))
                        director.save()
                if elem.get('actor_1'):
                    try:
                        actor_1 = Person.objects.get(name=elem.get('actor_1'))
                    except ObjectDoesNotExist:
                        actor_1 = Person(name=elem.get('actor_1'))
                        actor_1.save()
                if elem.get('actor_2'):
                    try:
                        actor_2 = Person.objects.get(name=elem.get('actor_2'))
                    except ObjectDoesNotExist:
                        actor_2 = Person(name=elem.get('actor_2'))
                        actor_2.save()
                if elem.get('actor_3'):
                    try:
                        actor_3 = Person.objects.get(name=elem.get('actor_3'))
                    except ObjectDoesNotExist:
                        actor_3 = Person(name=elem.get('actor_3'))
                        actor_3.save()
                fun_facts = elem.get('fun_facts')

                try:
                    city_film_loc = CityFilmLoc.objects.get(movie_id=movie, location_id=location)
                except ObjectDoesNotExist:
                    city_film_loc = CityFilmLoc(movie_id=movie, location_id=location, fun_facts=fun_facts, production_company_id=production_company, distributor_id=distributor, director_id=director, writer_id=writer, actor_1_id=actor_1, actor_2_id=actor_2, actor_3_id=actor_3)
                    city_film_loc.save()
        except Exception as e:
            print e

    print "Data Dump Complete!!"

processData()