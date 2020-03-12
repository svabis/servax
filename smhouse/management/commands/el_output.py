# -*- coding: utf-8 -*-
from __future__ import division
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError
from smhouse.models import ElConsumption

temp_month = [-4.7, -4.2, -0.5, 5.1, 11.4, 15.5, 16.9, 16.2, 12, 7.4, 2.1, -2.3]
life = [0,0,0,1,1,1,1,1,1,1,1,1]
heat = [0,0,0,1,0,0,0,0,1,1,1,1]

# command
class Command(BaseCommand):
  help = "Genereate average dayly output"
  def handle(self, *args, **options):

   # get last data for this year
    el = ElConsumption.objects.all().order_by('-date')[:18]
    el = reversed( el )

   # make reversed able to call by index again
    temp = []
    for e in el:
      temp.append( e )
    el = temp

   # set initail values for iterating
    temp_read = el[0].read
    temp_date = el[0].date
   # starting count backwards
    temp_day_nr = 0


   # print table header
#    print( "DATE\t\tDIENAS\tRADIJUMS\tPATERINS\tPATERINS/DIENĀ\tTEMPERATURE" )
    print( "DAY\tAVERAGE\tTEMPERATURE" )

   # iterate DB objects
    for e in el:
#      print( str(e.date.timetuple().tm_yday) + "\t" + str(temp_read) )
      for i in range(temp_day_nr, e.date.timetuple().tm_yday):
#        print( str(i) + "\t" + str(e.cons_days) + "\t\t" + str(temp_month[e.date.month-1]) )

#        print( "[" + str(temp_month[e.date.month-1]) + ", " + str(e.cons_days) + ", " + str(life[e.date.month-1]) + ", " + str(heat[e.date.month-1]) + "]," )
        print( "[" + str(heat[e.date.month-1]) + "]," )

     # save object fields
      temp_read = e.read
      temp_date = e.date
      temp_day_nr = e.date.timetuple().tm_yday
