# -*- coding: utf-8 -*-
from django.http import HttpResponse # for Live_Users counter response
from django.shortcuts import render, redirect # response to template, redirect to another view

from django.utils import timezone # for Live_video visits

from video.models import Camera, Video	# import aplication models
from login.models import User_data, Live_video # Access data

from main.args import create_args

from datetime import datetime, date, timedelta
import uuid


# ============================================================================================
# LIVE VIDEO
def live(request):
    args = create_args(request)
    args['title'] = 'Video dzīvajā | Svabwilla'
    args['heading'] = 'Video dzīvajā'

   # enable zoom on mobile device
    args["mobile_zoom"] = True

    if args['username'].get_username() == '': # NO USER
        return redirect( 'access_denied' )
    else:
        video_live = User_data.objects.get(user_user = args['username']).video_live

    if video_live:
# ACCESS ALLOWED -->
      # creating args
        args['cameras'] = Camera.objects.filter( cam_visible = True ).order_by('cam_nr')
        response = render( request, 'mobile.html', args )
        response.set_cookie( key='page_loc', value='/video/live/', path='/' )

       # check uuid cookie
        c_value = uuid.uuid4()
        if 'video_live' in request.COOKIES:
            c_value = request.COOKIES.get('video_live')
            response.set_cookie( key='video_live', value=c_value, max_age=900 )

       # new "Live_Video" session detected: creation DB entry
        else:
             Live_video.objects.create( user = args['username'], mobile = args['mobile_browser'], tablet=args['tablet_browser'], cookie_uuid=c_value )

        response.set_cookie( key='video_live', value=c_value, max_age=900 )
        return response

    return redirect( 'access_denied' )


# ============================================================================================
# LIVE STREAM
def stream(request):
    args = create_args(request)
    args['title'] = 'Video dzīvajā | Svabwilla'
    args['heading'] = 'Video dzīvajā'

    if args['username'].get_username() == '': # NO USER
        return redirect( 'access_denied' )
    else:
        video_live = User_data.objects.get(user_user = args['username']).video_live

    if video_live:
# ACCESS ALLOWED -->

        args['cameras'] = Camera.objects.filter( cam_visible = True).order_by('cam_nr')
#        args['cameras'] = Camera.objects.filter( cam_visible = True, stream=True ).order_by('cam_nr')

        response = render( request, 'stream.html', args )
        response.set_cookie( key='page_loc', value='/video/stream/', path='/' )

       # check uuid cookie
        c_value = uuid.uuid4()
        if 'video_live' in request.COOKIES:
            c_value = request.COOKIES.get('video_live')
            response.set_cookie( key='video_live', value=c_value, max_age=900 )

       # new "Live_Video" session detected: creation DB entry
        else:
            Live_video.objects.create( user = args['username'], mobile = args['mobile_browser'], tablet=args['tablet_browser'], cookie_uuid=c_value )

        response.set_cookie( key='video_live', value=c_value, max_age=900 )
        return response

# ACCESS DENIED -->
    else:
        return redirect( 'access_denied' )


# ============================================================================================
# LEAVE TIME AJAX FOR "LIVE VIDEO"
def leave_video(request):
    args = create_args(request)

   # check uuid cookie
    c_value = uuid.uuid4()
    if 'video_live' in request.COOKIES:
        c_value = request.COOKIES.get('video_live')
        try:
           temp = Live_video.objects.get( user = args['username'], cookie_uuid=c_value )
           temp.leave = timezone.now()
          # calculate time elapsed watching
           t = temp.leave - temp.visit
           visit_time = (datetime.min + t).time()
           temp.time = visit_time
           temp.save()
        except:
           pass

        response = HttpResponse('ok')
        response.set_cookie( key='page_loc', value='/video/live/', path='/' )
        response.set_cookie( key='video_live', value=c_value, max_age=900 ) #datetime.now() + timedelta(minutes=10) )
        return response

    return HttpResponse('done')


# ============================================================================================
# TURNING ALL CAMERAS ON
def all_cam_on(request):
    for k in Camera.objects.all():
        k.cam_visible = True
        k.save()
    return redirect('/video/live/')


