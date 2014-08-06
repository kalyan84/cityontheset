from django.conf.urls import patterns, include, url
from django.contrib import admin

import os, sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path += [PROJECT_ROOT]

from cityontheset.src import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cityontheset/api/movies', views.MoviesList.as_view()),
    url(r'^cityontheset/api/cityfilmlocs', views.CityFilmLocsList.as_view()),
    url(r'^', views.CityFilmLocsView),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
