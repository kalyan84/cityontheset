__author__ = 'kalyang'

from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    release_year = models.IntegerField(max_length=4)

    class Meta:
        db_table = 'movies'
        managed = False

class Location(models.Model):
    name = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=17, decimal_places=14,blank=True)
    lng = models.DecimalField(max_digits=17, decimal_places=14,blank=True)

    class Meta:
        db_table = 'locations'
        managed = False

class Person(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'persons'
        managed = False

class Company(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'companies'
        managed = False

class CityFilmLoc(models.Model):
    movie_id = models.ForeignKey(Movie, db_column='movie_id', verbose_name='Movie')
    location_id = models.ForeignKey(Location, db_column='location_id', verbose_name='Location', blank=True, null=True)
    fun_facts = models.TextField(blank=True, null=True)
    production_company_id = models.ForeignKey(Company, db_column='production_company_id', verbose_name='Production Company', blank=True, null=True)
    distributor_id = models.ForeignKey(Company, db_column='distributor_id', verbose_name='Distributor', blank=True, null=True)
    director_id = models.ForeignKey(Person, db_column='director_id', verbose_name='Director', blank=True, null=True)
    writer_id = models.ForeignKey(Person, db_column='writer_id', verbose_name='Writer', blank=True, null=True)
    actor_1_id = models.ForeignKey(Person, db_column='actor_1_id', verbose_name='Actor 1', blank=True, null=True)
    actor_2_id = models.ForeignKey(Person, db_column='actor_2_id', verbose_name='Actor 2', blank=True, null=True)
    actor_3_id = models.ForeignKey(Person, db_column='actor_3_id', verbose_name='Actor 3', blank=True, null=True)

    class Meta:
        db_table = 'city_film_locs'
        managed = False