# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from jobs.models import Jobs, JobsTypes

from login.models import User_data

from main.args import create_args

from datetime import datetime, date, timedelta
#import itertools	# Nested Counter

from jobs.views.jobs_sort import *

# JOBS ARGS LIST
def default(request):
    args = create_args(request)
    args['title'] = 'Darbu saraksts | Svabwilla'
    args['heading'] = "Darbu saraksts"

    args['type'] = JobsTypes.objects.all()

   # User Restrictions
    try:
        args['u_job_list'] = User_data.objects.get(user_user = args['username']).job_list
        args['u_job_start'] = User_data.objects.get(user_user = args['username']).job_start
        args['u_job_fin'] = User_data.objects.get(user_user = args['username']).job_fin
        args['u_job_cancel'] = User_data.objects.get(user_user = args['username']).job_cancel
        args['u_job_mark'] = User_data.objects.get(user_user = args['username']).job_mark
#        args['job_restart'] = User_data.objects.get(user_user = args['username']).job_fin
    except:
        args['u_job_list'] = args['u_job_start'] = args['u_job_fin'] = args['u_job_cancel'] = args['u_job_mark'] = False
#        args['u_job_list'] = args['u_job_start'] = args['u_job_fin'] = args['u_job_cancel'] = args['u_job_mark'] = args['job_restart'] = False
    return args


# =====================================================
# SORT READ FROM COOKIE
def cookie_sort(request, sort, cookie):
    if str(cookie) in request.COOKIES:
        if sort == 0:
            sort = int(request.COOKIES.get(str(cookie))) # RENEW SORT FROM LAST LOCATION
        else:
            if request.COOKIES.get('ret') != 'True':
               # REVERSE COLUMN SORT
                sort_save = int(request.COOKIES.get(str(cookie)))
                mysort = [1,3,5,7,9]
                for n in mysort:
                    if (sort_save == int(n) or sort_save == int(n)+1) and (int(sort) == int(n) or int(sort) == int(n)+1):
                        if sort_save == int(sort) and  int(sort) == int(n):
                            sort = int(n)+1
                        else:
                            sort = n
    else: # EMPTY SORT ARGUMENT
        sort = 1
    return sort


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! MARKED JOBS VIEW !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# JOBS LINK FROM LEFT MENU
def jobs_main(request):
    response = redirect('marked_job_list')
    response.delete_cookie('jobs_scroll')
    return response


# MARKED JOBS LIST
def marked(request):
   # if there are no marked jobs --> redirect to main
    if Jobs.objects.filter(marked=True).count() == 0:
        return redirect('main_job_list')

    args = default(request)
#    args.update(csrf(request))      # ADD CSRF TOKEN

    args['active_tab'] = 1
    args['unmarking'] = True

# RESTRICT ACCESS
    if args['u_job_list'] == False:
        return redirect('access_denied')
    elif args['username'].is_superuser:
        args['jobs'] = Jobs.objects.filter(marked=True).order_by('marked_id')
    else:
        args['jobs'] = Jobs.objects.filter(marked=True, jobs_zone__special=False).order_by('marked_id')

    response = render( request, 'marked.html', args )
    response.set_cookie( key='page_loc', value='/jobs/marked/', path='/' )
    return response


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! TO_DO VIEWS START !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# JOBS TO DO LIST
def to_do(request, sort_id=0):
    if int(sort_id) < 0 or int(sort_id) > 8:
        return redirect('/')

    sort = cookie_sort(request, sort_id, 'jobs_to_do_sort' )
    args = default(request)
#    args.update(csrf(request))      # ADD CSRF TOKEN

    args['active_tab'] = 2
    args['sort'] = int(sort)
    args['marking'] = True

# RESTRICT ACCESS
    if args['u_job_list'] == False:
        return redirect('access_denied')
    elif args['username'].is_superuser:
        j = Jobs.objects.filter(jobs_done=False, jobs_cancel=False, marked=False)
    else:
        j = Jobs.objects.filter(jobs_done=False, jobs_cancel=False, marked=False, jobs_zone__special=False)

    args['jobs'] = sort_options[int(sort)](j)

    if int(sort) == 1 or int(sort) == 2:
        response = render( request, 'to_do_by_date.html', args )
    else:
        response = render( request, 'to_do.html', args )

    response.set_cookie( key='jobs_to_do_sort', value=sort )
    response.set_cookie( key='page_loc', value='/jobs/to_do/' + str(sort) + '/', path='/' )
    return response


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DONE VIEWS START !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# JOBS COMPLEATED LIST
def done(request, sort_id=10):
    if int(sort_id) < 0 or int(sort_id) > 10 or int(sort_id) == 7 or int(sort_id) == 8:
        return redirect('/')

    sort = cookie_sort( request, sort_id, 'jobs_done_sort' )
    args = default(request)
    args['active_tab'] = 3
    args['sort'] = int(sort)

# RESTRICT ACCESS
    if args['u_job_list'] == False:
        return redirect('access_denied')
    elif args['username'].is_superuser:
        j = Jobs.objects.filter(jobs_done=True)
    else:
        j = Jobs.objects.filter(jobs_done=True, jobs_zone__special=False)

    args['jobs'] = sort_options[int(sort)](j)

    if int(sort) == 1 or int(sort) == 2 or int(sort) == 9 or int(sort) == 10:
        response = render( request, 'done_by_date.html', args )
    else:
        response = render( request, 'done.html', args )

    response.set_cookie( key='jobs_done_sort', value=sort )
    response.set_cookie( key='page_loc', value='/jobs/done/' + str(sort) + '/', path='/' )
    return response


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! CANCELED VIEWS START !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# CANCELED JOBS LIST
def canceled(request, sort_id=0):
    if int(sort_id) < 0 or int(sort_id) > 8:
        return redirect('/')

    sort = cookie_sort(request, sort_id, 'jobs_canceled_sort' )
    args = default(request)
    args['active_tab'] = 4
    args['sort'] = int(sort)

# RESTRICT ACCESS
    if args['u_job_list'] == False:
        return redirect('access_denied')
    elif args['username'].is_superuser:
        j = Jobs.objects.filter(jobs_cancel=True)
    else:
        j = Jobs.objects.filter(jobs_cancel=True, jobs_zone__special=False)

    args['jobs'] = sort_options[int(sort)](j)

    if int(sort) == 1 or int(sort) == 2 or int(sort) == 9 or int(sort) == 10:
        response = render( request, 'canceled_by_date.html', args )
    else:
        response = render( request, 'canceled.html', args )

    response.set_cookie( key='jobs_canceled_sort', value=sort )
    response.set_cookie( key='page_loc', value='/jobs/canceled/' + str(sort) + '/', path='/' )
    return response
