# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect # response to template, redirect to another view
from django.template import RequestContext # for 404 & 500 Error pages

# ====================== ERROR PAGES ========================
def handler404(request, *args, **argv):
    response = render(request, '404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request, *args, **argv):
    response = render(request, '500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response

# ========================== VIEWS ==========================
from login.models import User_data, Live_video
from main.args import create_args


# !!!!! DST !!!!!
def dst(test_date):
    import datetime
    import calendar
    test_day = test_date.date()
    year = test_day.year

    dst_start = max(week[-1] for week in calendar.monthcalendar(year, 10)) # last sunday of this years Oct
    dst_end   = max(week[-1] for week in calendar.monthcalendar(year, 3))  # last sunday of this years Mar
   # convert to date objects
    date_dst_start = datetime.date(year, 10, dst_start)
    date_dst_end = datetime.date(year, 3, dst_end)
   # compare if in range (summer --> True)
    if date_dst_end <= test_day <= date_dst_start:
        return test_date + datetime.timedelta(hours=3)
    else:
        return test_date + datetime.timedelta(hours=2)

# ACCESS DENIED
def denied(request):
    args = create_args(request)
    response = render(request, 'denied.html', args)
    response.set_cookie( key='page_location', value='/denied/' )
    return response


# MAIN PAGE
def home(request):
    args = create_args(request)
    args['title'] = 'Svabwilla'

    response = render(request, 'home.html', args)
    response.set_cookie( key='page_loc', value='/', path='/' )
    return response


# LOCATION
def location(request):
    args = create_args(request)
    args['title'] = 'Atrašanās vieta | Svabwilla'
    args['heading'] = 'Atrašanās vieta'

    response = render(request, 'map.html', args)
    response.set_cookie( key='page_loc', value='/location/', path='/' )
    return response


# WEATHER
def weather(request):
    args = create_args(request)
    args['title'] = 'Laika prognoze | Svabwilla'
    args['heading'] = 'Laika prognoze'

    response = render(request, 'weather.html', args)
    response.set_cookie( key='page_loc', value='/weather/', path='/' )
    return response


# STATISTIC
def stats(request):
    args = create_args(request)
    args['title'] = 'Statistika | Svabwilla'
    args['heading'] = 'Statistika'

   # DISK USAGE
    import os
    head = os.popen("df -h | grep Filesystem").read().replace("\n", "").split(" ")[:-1]
    while '' in head:
      head.remove('')
    args['df_head'] = head

    rez = []
    temp = os.popen("df -h | grep /dev/sd").read().split("\n")
    for t in temp:
        rez.append( t.split(" ") )

    rez.append( os.popen("df -h | grep /var/www/").read().replace("\n", "").split(" ") )
    for r in rez:
      while '' in r:
        r.remove('')
    args['df'] = rez

   # "Live video" ACTIVITY
    from datetime import datetime, timedelta
#    import pytz
#    tz = pytz.timezone('UTC')
   # now
    start = datetime.now()
   # 24h
    end = (start - timedelta(hours=24))
   # 7days
    week_end = (start - timedelta(days=7))

    video_stat = Live_video.objects.filter(visit__range=[week_end, start]).order_by('-visit')
    vid = []

   # days in different colors
    temp_day = dst(video_stat[0].visit).day
    day = 0
    for v in video_stat:
       # set day color
        if dst(v.visit).day != temp_day:
            day = 1 if day == 0 else 0
            temp_day = dst(v.visit).day

       # set 24h/7day
        if end <= dst(v.visit).replace(tzinfo=None) <= start:
            vid.append([0, day, v])
        else:
            vid.append([1, day, v])

    args['video'] = vid

    response = render(request, 'stat.html', args)
    response.set_cookie( key='page_loc', value='/stat/', path='/' )
    return response
