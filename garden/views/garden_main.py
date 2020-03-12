# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from login.models import User_data # Access data
from main.args import create_args

# -*- coding: utf-8 -*-
from django.contrib.auth.models import User     # Django Users library
from django.contrib import auth # autorisation library

from garden.paginator import Paginator # import paginator

from garden.models import SuperTheme, Theme, Post
from garden.forms import PostForm, ThemeForm

import unicodedata
import slugify
import math
import random
import string

# ================================================================================
# MAIN SKATS --> Visas Temas
def main(request, pageid=1):
    args = create_args(request)
    if args['username'].get_username() == '': # NO USER
        return redirect('access_denied')
    else:
        garden_access = User_data.objects.get(user_user = args['username']).garden
    if garden_access != True:
      # ACCESS DENIED
        return redirect('access_denied')

    try:
        args['garden_add'] = User_data.objects.get(user_user = args['username']).garden_add
    except:
        pass

    args['super'] = SuperTheme.objects.all().order_by('order')
    args['user'] = auth.get_user(request)

    args['heading'] = u'Dārzs | Visas tēmas'
    args['active_tab'] = "visas"

    args['disable_back'] = True

    results_per_page = 15

    rez_obj = Theme.objects.filter( comment = True ).order_by('-last_entry')

    if int(pageid) < 1: # negative page number --> 404
        return redirect ('/garden/')

    pagecount = int(math.ceil( int(rez_obj.count()) / float( results_per_page ))) # integer identical to range by count

    if int(pageid) > pagecount and int(pageid) > 1: # pageid exceeds pagecount --> 404
        return redirect ('/garden/')

    start_obj = int(pageid) * results_per_page - results_per_page # start from image NR
    end_obj = int(pageid) * results_per_page # end with image NR
    if end_obj > rez_obj.count(): # if end NR exceeds limit set it to end NR
        end_obj = rez_obj.count()

    args['paginator'] = Paginator( pagecount, pageid )
    args['temas'] = rez_obj[start_obj:end_obj]

    response = render(request, 'theme.html', args)
    response.set_cookie( key='page_loc', value='/garden/page=' + str(pageid) + '/' )
    return response


# ================================================================================
# SUPER TEMAS (Izvele pa kategorijam)
def super(request, s_id, pageid=1):
    args = create_args(request)
    if args['username'].get_username() == '': # NO USER
        return redirect('access_denied')
    else:
        garden_access = User_data.objects.get(user_user = args['username']).garden
    if garden_access != True:
      # ACCESS DENIED
        return redirect('access_denied')

    try:
        args['garden_add'] = User_data.objects.get(user_user = args['username']).garden_add
    except:
        pass

    try:
        s = SuperTheme.objects.get(slug=str(s_id))
    except:
        redirect('/garden/')

    args['super'] = SuperTheme.objects.all().order_by('order')
    args['user'] = auth.get_user(request)

    args['heading'] = u'Dārzs | ' + s.title
    args['active_tab'] = s.slug

    args['disable_back'] = True

    rez_obj = Theme.objects.filter( relate_to_super = s, parent = None ).order_by('comment', '-last_entry')

    results_per_page = 15

    if int(pageid) < 1: # negative page number --> 404
        return redirect ('/garden/')

    pagecount = int(math.ceil( int(rez_obj.count()) / float( results_per_page ))) # integer identical to range by count

    if int(pageid) > pagecount and int(pageid) > 1: # pageid exceeds pagecount --> 404
        return redirect ('/garden/')

    start_obj = int(pageid) * results_per_page - results_per_page # start from image NR
    end_obj = int(pageid) * results_per_page # end with image NR
    if end_obj > rez_obj.count(): # if end NR exceeds limit set it to end NR
        end_obj = rez_obj.count()

    args['paginator'] = Paginator( pagecount, pageid )
    args['temas'] = rez_obj[start_obj:end_obj]

    args['add_tema'] = True
    args['form'] = ThemeForm

    response = render(request, 'theme.html', args)
    response.set_cookie( key='page_loc', value='/garden/' + str(s_id) + '/' )
    return response
