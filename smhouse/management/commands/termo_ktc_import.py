# -*- coding: utf-8 -*-
from __future__ import division
from datetime import datetime

from django.conf import settings
from django.utils.timezone import make_aware

from django.core.management.base import BaseCommand, CommandError
from smhouse.models import TermoAdress, TermoPlace, TermoReading

import re
import os

#path = '/var/log/remotelogs/172.16.20.250/'
path = '/home/alex/termo_dati_ktc'

# command
class Command(BaseCommand):
    help = "Create objects for Adress ķesterciems"
    def handle(self, *args, **options):
        # Get KTC Termo Places relative to log files
         ktc = TermoAdress.objects.get(slug='ktc')
         termo_obj = TermoPlace.objects.filter(where=ktc)

         for filename in os.listdir(path):
           print(filename)

          # iterate TermoPlace objects in ktc
           for t in termo_obj:
#             print( t )
             try:
              # Read log file
               with open(path + filename, 'r') as f:
                   lines = f.read().splitlines()
#                   last_line = lines[-1]

               for last_line in lines:

                # get datetime from string
                 dtime = make_aware( datetime.strptime(last_line[0:16], '%Y-%m-%dT%H:%M') )
                # get temerature & humidity
                 rez = re.search(t.regex, last_line)

                 temp_rez = rez.group(1).split(":")
                # temperature
                 temp = temp_rez[0]
                 if "." not in temp:
                     temp = temp[:-1] + "." + temp[-1:]
                # humidity
                 try:
                     data = [dtime, float(temp), float( temp_rez[1] )]
                 except:
                     data = [dtime, float(temp), None]

#                 print( data )

                # Try to create new reading
                 try:
                     temp = TermoReading.objects.get( place = t, date = data[0] )
                 except:
                     temp = TermoReading( place = t, date = data[0], temp = data[1], humy = data[2] )
                     temp.save()

            # SKIP object
             except:
                 pass

#             print()
