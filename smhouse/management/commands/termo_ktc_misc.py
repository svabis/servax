# -*- coding: utf-8 -*-
from __future__ import division
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError
from smhouse.models import TermoAdress, TermoPlace, TermoReading

import re
import os

path = '/var/log/remotelogs/172.16.20.250/'
log_files = ['kscboardtemp.sh.log', 'myhost.log', 'pi.log']

last =["2020-03-21T11:40:01+02:00 upnix kscboardtemp.sh[2383]: .1.3.6.1.4.1.14988.1.1.3.10.0 = INTEGER: -390",
       "2020-03-21T11:42:51+02:00 ksc_termo myhost tempSensor: 12.90:65.00/3.60:99.90/-2.90:99.90",
       "2020-03-21T11:37:48+02:00 raspberrypi pi: temp=-41.9'C"]

re_str = ["= INTEGER: (-?\d{1,4})",
          "tempSensor: (-?\d{1,2}\.\d{1,2}\:\d{1,2}\.\d{1,2})/(-?\d{1,2}\.\d{1,2}\:\d{1,2}\.\d{1,2})/(-?\d{1,2}\.\d{1,2}\:\d{1,2}\.\d{1,2})",
          "temp=(-?\d{1,3}\.\d{1,2})'C"]


# command
class Command(BaseCommand):
    help = "Create objects for Adress ķesterciems"
    def handle(self, *args, **options):
        # Get KTC Termo Places relative to log files
         ktc = TermoAdress.objects.get(slug='ktc')
         termo_obj = TermoPlace.objects.filter(where=ktc)
         print( termo_obj )

         readings = TermoReading.objects.all() #filter( place = termo_obj )
         print( readings.count() )

         for r in readings:
             r.delete()
         return

        # define empty array for objects to be created
         data = []
         for i, last_line in enumerate(last):
                 print( last_line )

                # get datetime from string
                 dtime = datetime.strptime(last_line[0:16], '%Y-%m-%dT%H:%M')

                # get temerature & humidity
                 rez = re.search(re_str[i], last_line)

                 for r in range(1, len(rez.groups())+1 ):
                     temp = rez.group(r).split(":")
                    # temperature
                     t = temp[0]
                     if "." not in t:
                         t = t[:-1] + "." + t[-1:]
                    # humidity
                     try:
                         data.append([dtime, float(t), float(temp[1])])
                     except:
                         data.append([dtime, float(t), None])

         for d in data:
             print( d )
#         print( len(data) )
         return

         if len(data) == 5:
             for i, t in enumerate(termo_obj):
                 try:
                     temp = TermoReading.objects.get( place = t, date = data[i][0] )
#                     print( temp )
                 except:
                     temp = TermoReading( place = t, date = data[i][0], temp = -12.34, humy = data[i][2] )
                     temp.save()
#                     print( "SAVED: ", data[i] )


# mikrotik switch CPU temp 430 -> 43.0
# skapis/pieliekamias/ārs
# raspberry CPU

# 2020-03-20T20:20:01+02:00 upnix kscboardtemp.sh[28773]: .1.3.6.1.4.1.14988.1.1.3.10.0 = INTEGER: 430
# 2020-03-20T20:17:54+02:00 ksc_termo myhost tempSensor: 17.30:69.40/7.30:99.90/4.20:99.90
# 2020-03-20T20:17:49+02:00 raspberrypi pi: temp=45.1'C
