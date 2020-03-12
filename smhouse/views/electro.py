# -*- coding: utf-8 -*-
from __future__ import division
from django.shortcuts import render, redirect # response to template, redirect to another view

from login.models import User_data # Access data

from smhouse.models import ElConsumption

from main.args import create_args

from datetime import datetime, timedelta
today = datetime.now()


#!!!!! ELEKTRO MAIN !!!!!
def smhouse_electro_main(request):
    args = create_args(request)

# RESTRICT ACCESS
    if args['username'].get_username() == '': # NO USER
        return redirect('access_denied')
    else:
        electr_access = User_data.objects.get(user_user = args['username']).sm_electr
    if electr_access != True:
        return redirect('access_denied')

# ACCESS GRANTED
    args['input_date'] = today

    args['heading'] = "Elektro Patēriņš"
    args['title'] = 'Gudrā Māja | Svabwilla'

    data = ElConsumption.objects.all().order_by( 'date' )
    if data.count() < 2:
        args['graf'] = False

    args['data'] = data
    args['input_read'] = data.reverse()[0]

    response = render( request, 'electro.html', args )
    response.set_cookie( key='page_loc', value='/sm_house/electro/', path='/' )
    return response


#=============================================================================
#!!!!! ELEKTRO INPUT DATA !!!!!
def smhouse_electro_input_data(request):
    args = create_args(request)
    if request.POST: # actions if login Form is submitted
       # get last data
        last = ElConsumption.objects.all().order_by( '-date' )[0]

#        if True:
        try:
            obj_date = request.POST.get('date', '')
            date = datetime.strptime( obj_date, '%Y/%m/%d')

            obj_value = request.POST.get('read', '')
            value = int( obj_value )

# !!!!!!!!!!!!!!!!!!!!!!
# !!!!! VALIDATION !!!!!
# !!!!!!!!!!!!!!!!!!!!!!

            new_data = ElConsumption( date = date, read = value )
           # calculate fields
            temp_cons = value - last.read
            temp_days = (date.date() - last.date).days
            if temp_days == 0:
              temp_days = 1
            temp_cons_days = float( temp_cons/temp_days )

           # fill fields
            new_data.cons = temp_cons
            new_data.days = temp_days
            new_data.cons_days = temp_cons_days

            new_data.save()
            return redirect('electro_main')
        except:
            pass

    return redirect('electro_main')
