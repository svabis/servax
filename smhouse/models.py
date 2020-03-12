# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models


# !!!!! ELEKTRO-PATĒRIŅŠ !!!!!
class ElConsumption(models.Model):
    class Meta():
        db_table = "sm_elekto_paterins"

    date = models.DateField( default = timezone.now )
    read = models.IntegerField()

    cons = models.IntegerField( null=True, blank=True )
    days = models.IntegerField( null=True, blank=True )

    cons_days = models.DecimalField( max_digits = 5, decimal_places = 3, null=True, blank=True )

    def __str__(self):
        return "Datums:" + str(self.date) + " Skaititajs:" + str(self.read)


# !!!!! LED !!!!!
class LedTimer(models.Model):
    class Meta():
        db_table = "sm_led"

    time = models.TimeField( default = timezone.now )

# [0]-pirmdiena ... [6]-svētdiena (pozīcija)
# 1/0 - True/False
    days = models.CharField( max_length = 7, default = "1111111" )

    color = models.CharField( max_length = 7, null=True, blank=True )
    bright = models.IntegerField( null=True, blank=True )

    effect = models.IntegerField( null=True, blank=True )

#    def __unicode__(self):
#        return self.time
