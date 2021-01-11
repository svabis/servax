# -*- coding: utf-8 -*-
#from django.http import HttpResponse # for Live_Users counter response
from django.shortcuts import render, redirect # response to template, redirect to another view

from django.utils import timezone # for Live_video visits

from video.models import Camera, Video, VideoDayComment
from login.models import User_data, Live_video

from main.args import create_args

from datetime import datetime, date, timedelta
#import uuid



def archive_main(request):
    args = create_args(request)
    args['heading'] = "Video Arhīvs"
    args['title'] = 'Video arhīvs | Svabwilla'

# RESTRICT ACCESS
    if args['username'].get_username() == '': # NO USER
        return redirect('access_denied')
    else:
        video_archive = User_data.objects.get(user_user = args['username']).video_archive
    if video_archive != True:
        return redirect('access_denied')
    else:
# ACCESS ALOWED
#        d = datetime.now().replace(day=1).date()
        d = ( datetime.now().replace(day=1) - timedelta(120) ).date()
#        args['data'] = Video.objects.filter( video_date__startswith = d )
#        args['data'] = Video.objects.filter( video_date__year = '2017', video_date__month = '05' )
        args['data'] = Video.objects.filter( video_date__range = [ d, datetime.now().date() ] )
#        args['data'] = Video.objects.all().order_by("-video_date")

        args['comments'] = VideoDayComment.objects.filter( date__range = [ d, datetime.now().date() ] )

        args['today'] = datetime.now()

        args['cam'] = Camera.objects.all()

    response = render( request, 'archive.html', args )
    response.set_cookie( key='page_loc', value='/video/archive/', path='/' )
    return response
