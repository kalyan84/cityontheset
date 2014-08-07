__author__ = 'kalyang'

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics

from models import CityFilmLoc, Movie
from serializers import CityFilmLocSerializer, MovieSerializer


def CityFilmLocsView(request):
    return render(request, "cityontheset.html", {})

class MoviesList(generics.ListAPIView):
    model = Movie
    serializer_class = MovieSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        id = request.QUERY_PARAMS.get('id', None)
        name = request.QUERY_PARAMS.get('name', None)
        sort = request.QUERY_PARAMS.get('sort', None)
        limit = request.QUERY_PARAMS.get('limit', None)

        if id:
            movies = movies.filter(id=id)
        if name:
            movies = movies.filter(name__icontains=name)
        if sort:
            movies = movies.order_by(sort)
        if limit:
            movies = movies[:limit]

        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

class CityFilmLocsList(generics.ListCreateAPIView):
    model = CityFilmLoc
    serializer_class = CityFilmLocSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        cityfilmlocs = CityFilmLoc.objects.all()
        id = request.QUERY_PARAMS.get('id', None)
        movie_id = request.QUERY_PARAMS.get('movie_id', None)
        name = request.QUERY_PARAMS.get('name', None)
        location_id = request.QUERY_PARAMS.get('location_id', None)
        limit = request.QUERY_PARAMS.get('limit', None)

        if id:
            cityfilmlocs = cityfilmlocs.filter(id=id)
        if movie_id:
            cityfilmlocs = cityfilmlocs.filter(movie_id=movie_id)
        if location_id:
            cityfilmlocs = cityfilmlocs.filter(location_id=location_id)
        if name:
            cityfilmlocs = cityfilmlocs.filter(movie_id__name__icontains=name)
        if limit:
            cityfilmlocs = cityfilmlocs[:limit]

        if cityfilmlocs.count() > 20:
            cityfilmlocs = cityfilmlocs[:20]

        serializer = CityFilmLocSerializer(cityfilmlocs, many=True)
        return Response(serializer.data)