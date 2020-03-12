# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect

from jobs.models import Jobs		# import aplication models
from jobs.forms import JobsForm 	# import FORM

from login.models import User_data

from main.args import create_args

from datetime import datetime, date, timedelta

from jobs.views.jobs_sort import *

# JOBS ARGS LIST
def default(request):
    args = create_args(request)
    args['title'] = 'Darbu saraksts | Svabwilla'
    args['heading'] = "Darbu saraksts"
    return args


# MARKED JOBS REORDER
def marked_reorder(request):
    args = default(request)
    if args['username'].get_username() == '': # NO USER -->
        return HttpResponse('fail')
    else:
        job_mark = User_data.objects.get(user_user = args['username']).job_mark

    if job_mark == False:
        return HttpResponse('fail')
# ACCESS GRANTED
    if request.POST:
       # counter
        c = 1
       # proces JSON data
        jdata = request.POST['data']
        jdata = jdata.replace('[', '').replace(']', '').replace('"','').split(',')
        for i in jdata:
           try:
               temp_job = Jobs.objects.get( id = int(i) )
               temp_job.marked_id = c
               temp_job.save()
               c += 1
           except:
               pass

    return HttpResponse('done')

# MARK SELECTED JOBS
def marking(request):
    args = default(request)
    if args['username'].get_username() == '': # NO USER -->
        return redirect('/')
    else:
        job_mark = User_data.objects.get(user_user = args['username']).job_mark

    if job_mark == False:
# ACCESS RESTRICTED
        return redirect('main_job_list')
    else:
# ACCESS GRANTED
        if request.POST:
            jobs = request.POST.get('mark_job_id', '')
            jobs = jobs.replace("[", "")
            jobs = jobs.replace("]", "")
            jobs = jobs.split(",")

        for j in jobs:
            temp = Jobs.objects.get(id=int(j))
            temp.marked = True
            if temp.jobs_type == "KUVALDA" or temp.jobs_type == "GRAVANI":
                temp.marked_until = datetime.now() + timedelta(days=7)
            else:
                temp.marked_until = datetime.now() + timedelta(days=3)
            temp.save()

    response = redirect('marked_job_list')
    response.delete_cookie('jobs_scroll')
    return response


# UNMARK SELECTED JOBS
def unmarking(request):
    args = default(request)
    if args['username'].get_username() == '': # NO USER -->
        return redirect('/')
    else:
        job_mark = User_data.objects.get(user_user = args['username']).job_mark

    if job_mark == False:
# ACCESS RESTRICTED
        return redirect('main_job_list')
    else:
# ACCESS GRANTED
        if request.POST:
            jobs = request.POST.get('unmark_job_id', '')
            jobs = jobs.replace("[", "")
            jobs = jobs.replace("]", "")
            jobs = jobs.split(",")

        for j in jobs:
            temp = Jobs.objects.get(id=int(j))
            temp.marked = False
            temp.marked_id = None
            temp.save()

    response = redirect('marked_job_list')
    return response


# JOB START ACTION
def job_start(request, job_id):
    args = default(request)
    args['active_tab'] = 5
    if args['username'].get_username() == '': # IF NO USER --> DEMO LIST
        job_start = True
    else:
        job_start = User_data.objects.get(user_user = args['username']).job_start

    if job_start:
        if args['username'].get_username() == '': # IF NO USER --> DEMO LIST
# RESTRICT ACCESS
            return redirect('/')
        else:
            job = Jobs.objects.get(id = int(job_id))
            job.jobs_date_start = datetime.now()
            job.save()

    if 'page_loc' in request.COOKIES:
        ret_loc = str(request.COOKIES.get('page_loc'))
    else:
        ret_loc = '/'

    response = redirect( ret_loc )
    response.set_cookie( 'ret', 'True', max_age=5 ) # 5 second Cookie for not changing sort order
    return response


# JOB FINISHED ACTION
def job_finish(request, job_id):
    args = default(request)
    if args['username'].get_username() == '':
        job_fin = True
    else:
        job_fin = User_data.objects.get(user_user = args['username']).job_fin

    if job_fin:
        if args['username'].get_username() == '': # IF NO USER --> DEMO LIST
# RESTRICT ACCESS
            return redirect('/')
        else:
            job = Jobs.objects.get(id = int(job_id))
            job.jobs_date_done = datetime.now()
            job.jobs_done = True
            job.marked = False
            job.marked_until = None
            job.save()

    if 'page_loc' in request.COOKIES:
        ret_loc = str(request.COOKIES.get('page_loc'))
    else:
        ret_loc = '/'

    response = redirect( ret_loc )
    response.set_cookie( 'ret', 'True', max_age=5 ) # 5 second Cookie for not changing sort order
    return response


# JOB CANCEL ACTION
def job_cancel(request, job_id):
    args = default(request)
    if args['username'].get_username() == '':
        job_cancel = True
    else:
        job_cancel = User_data.objects.get(user_user = args['username']).job_cancel

    if job_cancel:
        if args['username'].get_username() == '': # IF NO USER --> DEMO LIST
# RESTRICT ACCESS
            return redirect('/')
        else:
            job = Jobs.objects.get(id = int(job_id))
            job.jobs_cancel = True
            job.marked = False
            job.marked_until = None
            job.save()

    if 'page_loc' in request.COOKIES:
        ret_loc = str( request.COOKIES.get('page_loc') )
    else:
        ret_loc = '/'

    response = redirect( ret_loc )
    response.set_cookie( 'ret', 'True', max_age=5 ) # 5 second Cookie for not changing sort order
    return response
