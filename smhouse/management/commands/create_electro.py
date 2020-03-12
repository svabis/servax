# -*- coding: utf-8 -*-
from __future__ import division
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError
from smhouse.models import ElConsumption

temp_month = [-4.7, -4.2, -0.5, 5.1, 11.4, 15.5, 16.9, 16.2, 12, 7.4, 2.1, -2.3]


# command
class Command(BaseCommand):
  help = "Genereate average dayly output"
  def handle(self, *args, **options):

#    el = ElConsumption.objects.all().order_by('date')
#    el = ElConsumption.objects.all().order_by('-date')[:19]
#    el = reversed( el )

    temp_read = 0
#    temp_date = el[0].date

    print( "DATE\t\tDIENAS\tRADIJUMS\tPATERINS\tPATERINS/DIENĀ\tTEMPERATURE" )
#    start = False
    start = True

    for e in el:
#      print( str(e.date.timetuple().tm_yday) + "\t" + str(temp_read) )
#      if e.date.timetuple().tm_yday == 1:
#        start = True

      if temp_read != 0:
        e.cons = e.read - temp_read
        e.dienas = (e.date - temp_date).days
        try:
          e.cons_days = float(e.cons/e.days)
        except:
          pass
        e.save()


#      print str(e.date.timetuple().tm_yday) + "\t" + str(e.days) + "\t" + str(e.read) + "\t\t" + str(e.cons) + "\t\t" + str(e.cons_days)

      if start:
        print( str(e.date) + "\t" + str(e.days) + "\t" + str(e.read) + "\t\t" + str(e.cons) + "\t\t" + str(e.cons_days) + "\t\t" + str(temp_month[e.date.month-1]) )

     # save object fields
      temp_read = e.read
      temp_date = e.date
