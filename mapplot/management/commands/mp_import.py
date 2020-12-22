# -*- coding: utf-8 -*-
from __future__ import division
from datetime import datetime

from django.conf import settings
from django.utils.timezone import make_aware

from django.core.management.base import BaseCommand, CommandError
from mapplot.models import MapPlot
from mapplot.models import MapPlotCity

import re
import os


# command
class Command(BaseCommand):
    help = "Read TermoReading's from log files last lines"
    def handle(self, *args, **options):
       # Read log file
        with open("/home/alex/m.txt", 'r') as f:
            lines = f.read().splitlines()

        rx = '"name":"(\w+)","lat":(\w+),"lon":(\w+)}'
        rx = '"name":"(\w+)","lat":(\d+.\d+),"lon":(\d+.\d+)}'

        c1 = 0
        c2 = 0

        city = MapPlotCity.objects.get( id=1 )
        print(city)

       # iterate last lines
        for last_line in lines:
            try:
                rez = re.search(rx, last_line)
                print(rez.group(1), rez.group(2), rez.group(3))

                new = MapPlot(city=city, mark=rez.group(1), lat=rez.group(2), lon=rez.group(3))
                new.save()

                c1 += 1
            except:
                c2 += 1
                pass

        print(c1)
        print(c2)
