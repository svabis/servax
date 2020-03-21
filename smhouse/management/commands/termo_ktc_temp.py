# -*- coding: utf-8 -*-
from __future__ import division
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError
from smhouse.models import TermoAdress, TermoPlace, TermoReading

import re
import os

path = '/var/log/remotelogs/172.16.20.250/'

log_files = ['kscboardtemp.sh.log', 'myhost.log', 'pi.log']

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

         last_c = []

         last = []
         i = True
         c = 0
         while i == True:
           l_temp = []
           for log in log_files:
              try:
                with open(path + log, 'r') as f:
                  lines = f.read().splitlines()
                  l_temp.append( lines[c] )
              except:
                l_temp.append( None )
           if l_temp[0] == None and l_temp[1] == None and l_temp[2] == None:
              i = False
           last.append( l_temp )
           last_c.append( len(l_temp) )
           c += 1

         print( "rindas:   ", c )
         print( "ieraksti: ", len(last) )

# ===================================================================================

         for line in last:
          # define empty array for objects to be created
           data = []
           for i, last_line in enumerate(line):
#                 if last_line != None:
#                      print( last_line )
                 try:
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
                 except:
                   data.append( None )

          # Create objects
           if len(data) == 5:
             for i, t in enumerate(termo_obj):
                 if data[i] == None:
                     continue
                 try:
                     temp = TermoReading.objects.get( place = t, date = data[i][0] )
#                     print( temp )
                 except:
                     temp = TermoReading( place = t, date = data[i][0], temp = data[i][1], humy = data[i][2] )
                     temp.save()
#                     print( "SAVED: ", data[i] )


# mikrotik switch CPU temp 430 -> 43.0
# skapis/pieliekamias/ārs
# raspberry CPU

# 2020-03-20T20:20:01+02:00 upnix kscboardtemp.sh[28773]: .1.3.6.1.4.1.14988.1.1.3.10.0 = INTEGER: 430
# 2020-03-20T20:17:54+02:00 ksc_termo myhost tempSensor: 17.30:69.40/7.30:99.90/4.20:99.90
# 2020-03-20T20:17:49+02:00 raspberrypi pi: temp=45.1'C
