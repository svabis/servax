# -*- coding: utf-8 -*-
from __future__ import division
from datetime import datetime

from django.conf import settings
from django.utils.timezone import make_aware

from django.core.management.base import BaseCommand, CommandError
from smhouse.models import Location, TermoPlace, TermoReading

import re
import os


# command
class Command(BaseCommand):
    help = "Read TermoReading's from log files last lines"
    def handle(self, *args, **options):
       # get locations
        loc = Location.objects.all()
       # iterate Location's
        for l in loc:
            termo_obj = TermoPlace.objects.filter(where=l)

           # iterate TermoPlace objects in ktc
            for t in termo_obj:
                try:
                 # Read log file
                  with open(t.filename, 'r') as f:
                        lines = f.read().splitlines()
#                        last_lines = lines[-1000:-1]

                 # iterate last lines
                  for last_line in lines[-20:-1]:
#                  for last_line in lines[-7:-1]:

                    try:
#                      print(last_line)

                     # get datetime from string
                      dtime = make_aware( datetime.strptime(last_line[0:16], '%Y-%m-%dT%H:%M') )
                     # get temerature & humidity
                      rez = re.search(t.regex, last_line)
#                      print(rez)

                      temp_rez = rez.group(1).split(":")
                     # temperature
                      temp = temp_rez[0]
                      if "." not in temp:
                          temp = temp[:-1] + "." + temp[-1:]

                      temp = float(temp)
                     # ignore wrong temeratue readings
                      if temp > 95:
                          temp = None

                     # humidity
                      try:
                          data = [dtime, temp, float( temp_rez[1] )]
                      except:
                          data = [dtime, temp, None]

#                      print( data )

                     # Try to create new reading
                      try:
                          temp = TermoReading.objects.get( place = t, date = data[0] )
                      except:
                          temp = TermoReading( place = t, date = data[0], temp = data[1], humy = data[2] )
                          temp.save()

                    except:
                        print(last_line)
                        pass

               # SKIP object
                except:
                    pass
