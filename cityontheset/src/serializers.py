__author__ = 'kalyang'

from rest_framework import serializers

from models import Movie, Location, Person, Company, CityFilmLoc


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'release_year')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'lat', 'lng')

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name')

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name')

class CityFilmLocSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CityFilmLoc
        depth = 1
        fields = ('id', 'movie_id','location_id','fun_facts','production_company_id','distributor_id','director_id','writer_id','actor_1_id','actor_2_id','actor_3_id')