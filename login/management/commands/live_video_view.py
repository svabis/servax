# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

from django.conf import settings

from login.models import Live_video

from datetime import datetime, date, timedelta

from django.forms.models import model_to_dict
import json

import os


output = settings.MEDIA_ROOT + "live.json"
temp_output = settings.MEDIA_ROOT + "temp_live.json"

# JSON SERIALIZER datetime NO ERROR
def default(o):
    if isinstance(o, (date, datetime)):
        return o.isoformat()


# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):
#        print( settings.MEDIA_ROOT )
#        print( output )

        count = Live_video.objects.all().count()
        latest = Live_video.objects.all()[ count-1 ]

       # read last json from file
        with open( temp_output ) as f:
          last_data = json.load(f)

#        print( latest.id )
#        print( last_data["id"] )

        if latest.id != last_data["id"]:
            temp_json = "{ user:'" + str(latest.user) + "', visit:'" + str(latest.visit) + "'}"
        else:
            temp_json = "{}"

       # write live.json file
        file = open(output, "w")
        file.write( temp_json )
        file.close()

       # temp output
        dict_obj = model_to_dict( latest )
        temp_json = json.dumps( dict_obj, sort_keys=True, indent=1, default=default )

        file = open(temp_output, "w")
        file.write( temp_json )
        file.close()
