# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

from datetime import datetime


# !!!!! MAP PLOT CITY !!!!!
class MapPlotCity(models.Model):
    class Meta():
        db_table = "map_plot_city"

    name = models.CharField( max_length=20, default="" )

    def __str__(self):
        return self.name


# !!!!! MAP PLOT POINTS !!!!!
PLOT_TYPES = (
    ('yellow', 'stabs'),
    ('green', 'kaste'),
#    ('blue', 'zils'),
)

class MapPlot(models.Model):
#'date', 'mark', 'city', 'lat', 'lon', 'radio', 'chk_1', 'chk_2', 'chk_3'
    class Meta():
        db_table = "map_plot_points"

    date = models.DateTimeField( default = timezone.now )

    mark = models.CharField( max_length=8, default="" )

    city = models.ForeignKey( MapPlotCity, on_delete=models.CASCADE, default=1 )

    lat = models.CharField( max_length=50 )
    lon = models.CharField( max_length=50 )

    radio = models.CharField( max_length=10, choices=PLOT_TYPES, default="red")

    chk_1 = models.BooleanField( default=False )
    chk_2 = models.BooleanField( default=False )
    chk_3 = models.BooleanField( default=False )

   # dzēsts
    deleted = models.BooleanField( default=False )
   # ID dublikāti
    unique = models.BooleanField( default=True )

