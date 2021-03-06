# -*- coding: utf-8 -*-
from __future__ import division
from datetime import datetime, date

#from django.conf import settings
from django.utils.timezone import make_aware

from django.core.management.base import BaseCommand, CommandError
from smhouse.models import Location, SunData

import re
import os

# get data from url to json
#import json
import urllib.request

today = datetime.now()


# Open and read url
def get_data( url ):
    sunrise = ""
    sunset = ""
   # open url
    with urllib.request.urlopen( url ) as response:
        html = response.read()
    lines = html.splitlines()

    print(type(html))
    html = html.decode("utf-8")
    print(type(html))

    print(lines[116])

#    rez = []

#    for line in lines:
#    temp = re.findall('dateTime="(\d{2}\:\d{2})" class="celestial-events__text"', html)
    temp = re.findall("dateTime", html)

#    temp = re.search('dateTime', html)

#        rez.append(temp)
    print( temp )


#    for line in lines:
#        if b'Sunrise' in line:
#            print(line)
#            sunrise = line.split(b'>')[1].split(b'<')[0].decode("utf-8").split(" ")[1]
#        if b'Sunset' in line:
#            print(line)
#            sunset = line.split(b'>')[1].split(b'<')[0].decode("utf-8").split(" ")[1]

    return
    sunrise = make_aware( today.replace( hour=int(sunrise.split(":")[0]), minute=int(sunrise.split(":")[1]), second=0, microsecond=0 ) )
    sunset = make_aware( today.replace( hour=int(sunset.split(":")[0]), minute=int(sunset.split(":")[1]), second=0, microsecond=0 ) )
    return [ sunrise, sunset ]

#    return [0,0]

# command
class Command(BaseCommand):
    help = "Get sunset and sunrise for Location"
    def handle(self, *args, **options):
       # get locations
        loc = Location.objects.all()
       # iterate Location's
        for l in loc:
            data = get_data(l.sun_url)
#            print(data)

            try:
                temp = SunData.objects.get(date = today.date(), where=l)
            except:
                temp = SunData(where=l, sunrise=data[0], sunset=data[1])
                temp.save()
