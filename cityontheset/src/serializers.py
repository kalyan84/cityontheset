__author__ = 'kalyang'

from rest_framework import serializers

from models import Movies, Locations, Persons, Companies, CityFilmLocs


class MoviesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movies
        fields = ('id', 'name', 'release_year')

class LocationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Locations
        fields = ('id', 'name', 'lat', 'lng')

class PersonsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persons
        fields = ('id', 'name')

class CompaniesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Companies
        fields = ('id', 'name')

class CityFilmLocsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CityFilmLocs
        depth = 1
        fields = ('id', 'movie_id','location_id','fun_facts','production_company_id','distributor_id','director_id','writer_id','actor_1_id','actor_2_id','actor_3_id')