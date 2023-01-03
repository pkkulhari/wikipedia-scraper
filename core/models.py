from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    flag_link = models.URLField()
    capital = models.CharField(max_length=100)
    largest_city = models.CharField(max_length=100)
    official_languages = models.CharField(max_length=100)
    area_total = models.FloatField()
    population = models.IntegerField()
    gdp_nominal = models.CharField(max_length=100)
