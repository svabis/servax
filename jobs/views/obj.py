# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

#from jobs.forms import JobsForm 	# import FORM

from login.models import User_data	# import user_stats

from jobs.models import JobObj		# import aplication models

from main.args import create_args


def default(request):
    args = create_args(request)
    args['title'] = "Lietu parametri | Svabwilla"
    args['heading'] = "Lietu parametri"
    return args


# !!!!! OBJ LIST --> Tabs !!!!!
def obj_list(request):
    args = default(request)

# RESTRICT ACCESS
    if args['username'].get_username() == '': # NO USER
        return redirect('access_denied')
    elif User_data.objects.get(user_user = args['username']).obj_list != True: # no access
        return redirect('access_denied')
# ACCES GRANTED
    else:
        data = []
        for j in JobObj.objects.filter( obj_actual=True ).order_by('-obj_nr'):
             data.append([ j, j.o_i.all(), j.o_f.all() ])
        args['data'] = data

        old_data = []
        for j in JobObj.objects.filter( obj_actual=False ).order_by('-obj_added'):
             old_data.append([ j, j.o_i.all(), j.o_f.all() ])
        args['old_data'] = old_data

    response = render( request, 'obj_list.html', args )
    response.set_cookie( key='page_loc', value='/jobs/objects/', path='/' )
    return response


# !!!!! OLD OBJ LIST !!!!!
def orig_obj_list(request):
    args = default(request)

# RESTRICT ACCESS
    if args['username'].get_username() == '': # NO USER
        return redirect('access_denied')
    elif User_data.objects.get(user_user = args['username']).obj_list != True: # no access
        return redirect('access_denied')
# ACCES GRANTED
    else:
        data = []
        for j in JobObj.objects.filter( obj_actual=False ).order_by('-obj_added'):
             data.append([ j, j.o_i.all(), j.o_f.all() ])
        args['old_data'] = old_data

    response = render( request, 'obj_list.html', args )
    response.set_cookie( key='page_loc', value='/jobs/objects/', path='/' )
    return response
