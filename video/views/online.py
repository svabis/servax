# -*- coding: utf-8 -*-
from django.http import HttpResponse

from django.utils import timezone

from main.args import create_args

from login.models import Live_video

from datetime import datetime, date, timedelta

import pytz
tz = pytz.timezone('UTC')


# Notification Json about last user watching
def notificator(request):
    count = Live_video.objects.all().count()
    latest = Live_video.objects.all()[ count-1 ]

    leave_time = timezone.now() - timedelta(minutes=1)

#    if latest.leave > leave_time:
#        rez_json = '{ "user":"' + str(latest.user) + '", "visit":"' + str(latest.visit) + '", "left":"None"}'
#    else:
#        rez_json = '{ "user":"' + str(latest.user) + '", "visit":"' + str(latest.visit) + '", "left":"' + str(latest.leave) + '"}'

    rez_json = '{ "user":"' + str(latest.user) + '", "visit":"' + str(latest.visit) + '", "left":"' + str(latest.leave) + '"}'

    return HttpResponse(rez_json)

