__author__ = 'kalyang'

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics

from models import CityFilmLocs, Movies
from serializers import CityFilmLocsSerializer, MoviesSerializer


def CityFilmLocsView(request):
    return render(request, "CityOnTheSet.html", {})

class MoviesList(generics.ListAPIView):
    model = Movies
    serializer_class = MoviesSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        movies = Movies.objects.all()
        id = request.QUERY_PARAMS.get('id', None)
        name = request.QUERY_PARAMS.get('name', None)

        if(id):
            movies = movies.filter(id=id)

        if(name):
            movies = movies.filter(name__icontains=name).order_by('-release_year')

        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data)

class CityFilmLocsList(generics.ListCreateAPIView):
    model = CityFilmLocs
    serializer_class = CityFilmLocsSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        sffilmlocs = CityFilmLocs.objects.all()
        movie_id = request.QUERY_PARAMS.get('movie_id', None)
        name = request.QUERY_PARAMS.get('name', None)
#        release_year = request.QUERY_PARAMS.get('release_year', None)
#        location = request.QUERY_PARAMS.get('location', None)

        if movie_id is not None:
            sffilmlocs = sffilmlocs.filter(movie_id=movie_id)
        if name is not None:
            sffilmlocs = sffilmlocs.filter(movie_id__name__icontains=name)

        serializer = CityFilmLocsSerializer(sffilmlocs, many=True)
        return Response(serializer.data)