# -*- coding: utf-8 -*-
from django.http import HttpResponse # Response for Ajax POST
from django.shortcuts import render, redirect # response to template, redirect to another view

#from django.core.context_processors import csrf

from login.models import User_data # Access data

from main.args import create_args

import socket
import json

# !!!!! LED VIEW !!!!!
def smhouse_led(request):
    args = create_args(request)
    args['heading'] = "Apgaismojums"
    args['title'] = 'Gudrā Māja | Svabwilla'

# RESTRICT ACCESS
    if args['username'].get_username() == '': # NO USER
        return redirect('access_denied')
    else:
        elektr_access = User_data.objects.get(user_user = args['username']).sm_led
    if elektr_access != True:
        return redirect('access_denied')

# ACCESS GRANTED
    response = render( request, 'led.html', args )
    response.set_cookie( key='page_loc', value='/sm_house/led/', path='/' )
    return response



# !!!!! LED AJAX CONTROL --> socket --> Raspberrypi !!!!!
def led_control(request):
    args = create_args(request)
# RESTRICT ACCESS
    if args['username'].get_username() == '': # NO USER
        return HttpResponse('fail')
    else:
        elektr_access = User_data.objects.get(user_user = args['username']).sm_led
    if elektr_access != True:
        return HttpResponse('fail')

    resp = '{"RGB":[0, 0, 0]}'

    if request.POST:
       # proces JSON data
        jdata = request.POST['data']

       # RaspbberyPi socket data
        HOST = '172.16.5.90'
        PORT = 65432

        try:
            s = socket.socket()
            s.connect((HOST, PORT))
            s.send( bytes( jdata ) )
            data = s.recv(1024)

            j = json.loads(data)
            r = int( (j["RGB"][0]*j["B"])/255 )
            g = int( (j["RGB"][1]*j["B"])/255 )
            b = int( (j["RGB"][2]*j["B"])/255 )
            resp = '{"RGB":[' + str(r) + ', ' + str(g) + ', ' + str(b) + '], "B":' + str(j["B"]) + ', "S":' + str(j["S"]) + '}'
        except:
            pass

    return HttpResponse( resp )

