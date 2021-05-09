# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect

# import aplication models
from jobs.models import Jobs
# import FORM
from jobs.forms import JobsForm

from login.models import User_data

from main.args import create_args

from datetime import datetime, date, timedelta

from jobs.sorter import sort_marked_jobs

# JOBS ARGS LIST
def default(request):
    args = create_args(request)
    args['title'] = 'Darbu saraksts | Svabwilla'
    args['heading'] = "Darbu saraksts"
    return args


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ADD VIEWS START !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ADD NEW JOB
def add(request):
    args = default(request)
    job_add = False
    if args['username'].get_username() == '': # IF NO USER --> DEMO
# RESTRICT ACCESS
        return redirect('/')
    elif User_data.objects.get(user_user = args['username']).job_list != True: # no access
# RESTRICT ACCESS
        return redirect('/')
    else:
       # PASS User TO FORM
        add_job_form = JobsForm( user = args['username'].is_superuser, initial={'jobs_zone':'2', 'jobs_type':'3'} )

    if User_data.objects.get(user_user = args['username']).job_add: # allow jobs add
        job_add = True

    args['active_tab'] = 5

    sort_marked_jobs()

    if job_add != True:
       # ADD JOBS DENIED
        args['job_add_denied'] = True
    else:
       # ACCES GRANTED
        args['form'] = add_job_form
        if request.POST:	# FORM IS FILLED
            form = JobsForm( request.POST )
            if form.is_valid():
                temp = form.save( commit = False )

               # INSERT USERNAME WHO ADDED THIS JOB
                temp.jobs_user = args['username']

               # REPLACE LINE ENDS TO <br> TAGS
                temp.jobs_descr = (temp.jobs_descr).replace("\n", "<br>\n")

               # INITIAL JOB MARK
                if temp.marked == True:
                    if temp.marked == True:
                       # if days are set...
                        try:
                            time = int(request.POST.get('time', ''))
                            temp.marked_until = datetime.now() + timedelta(days=time)
                       # days are not specified
                        except:
                           # SET DAYS ACCORDING TO TYPE
                            if temp.jobs_type.marking_days is not None:
                                d = temp.jobs_type.marking_days
                            else:
                                d = 1
                            temp.marked_until = datetime.now() + timedelta(days = d)

                temp.save()
               # read REDIRECT
                red = str(request.POST.get('red', ''))

                response = None
                if red != "-":
                    response = redirect( 'menu_job' )
                else:
                    response = redirect( 'job_add' )
                response.set_cookie( key='job_added', value='true', path='/', max_age=5 )
                response.set_cookie( key='page_loc', value='/jobs/add/', path='/' )
                return response
            else:
                args['form'] = form	# ERROR MESSAGE

    response = render( request, 'add.html', args )
    response.set_cookie( key='page_loc', value='/jobs/add/', path='/' )
    return response
