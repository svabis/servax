# -*- coding: utf-8 -*-
from __future__ import division
from datetime import datetime

from django.conf import settings
from django.utils.timezone import make_aware

from django.core.management.base import BaseCommand, CommandError
from smhouse.models import Location, TermoPlace, TermoReading

#import tarfile
import re
import os



path = '/var/log/remotelogs/172.16.20.250/'
#path = '/home/alex/termo_dati_ktc/'

# command
class Command(BaseCommand):
    help = "Create objects for Adress ķesterciems"
    def handle(self, *args, **options):
        # Get KTC Termo Places relative to log files
         ktc = Location.objects.get(slug='ktc')
         termo_obj = TermoPlace.objects.filter(where=ktc).order_by('-order')

         for filename in os.listdir(path):

          # iterate TermoPlace objects in ktc
           for t in termo_obj:

# -----------------------------------------------------------
            # READ LOG
#             if filename.endswith("log"):
               with open(path + filename, 'r') as f:
                   lines = f.read().splitlines()

# -----------------------------------------------------------
            # READ .gz file
#             if filename.endswith(".gz"):
#              tar = tarfile.open(path + filename, "r:gz")
#              for member in tar.getmembers():
#               f = tar.extractfile(member)
#               if f is not None:
#                 lines = f.read()

               print( filename )
               print( t.regex )
               print()

               for last_line in lines:
                 try:

                  # get datetime from string                              2020-03-15T03:28
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

#                   print( data )

                  # Try to create new reading
                   try:
                     temp = TermoReading.objects.get( place = t, date = data[0] )
                   except:
                     temp = TermoReading( place = t, date = data[0], temp = data[1], humy = data[2] )
                     print( temp )
                     temp.save()

            # SKIP object
                 except:
                   pass

#             print()
