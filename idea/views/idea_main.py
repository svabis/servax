# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from login.models import User_data # Access data
from main.args import create_args

# -*- coding: utf-8 -*-
from django.contrib.auth.models import User     # Django Users library
from django.contrib import auth # autorisation library

from main.paginator import Paginator # import paginator

from idea.models import SuperTheme, Theme, Post
from idea.forms import ThemeForm

#import unicodedata
#import slugify
import math
#import random
#import string

# ================================================================================
# MAIN SKATS --> Visas Temas
def main(request, pageid=1):
    args = create_args(request)
    if args['username'].get_username() == '': # NO USER
        return redirect('access_denied')
    else:
        garden_access = User_data.objects.get(user_user = args['username']).idea
    if garden_access != True:
      # ACCESS DENIED
        return redirect('access_denied')

    try:
        args['garden_add'] = User_data.objects.get(user_user = args['username']).idea_add
    except:
        pass

    args['super'] = SuperTheme.objects.all().order_by('order')
    args['user'] = auth.get_user(request)

    args['title'] = u'Ideju Lāde | Visas idejas'
    args['heading'] = u'Ideju Lāde'
    args['active_tab'] = "visas"

    args['disable_back'] = True

    results_per_page = 5

    rez_obj = Theme.objects.filter( comment = True ).order_by('-last_entry')

    if int(pageid) < 1: # negative page number --> 404
        return redirect ('/idea/')

    pagecount = int(math.ceil( int(rez_obj.count()) / float( results_per_page ))) # integer identical to range by count

    if int(pageid) > pagecount: # pageid exceeds pagecount --> 404
        return redirect ('/idea/')

    start_obj = int(pageid) * results_per_page - results_per_page # start from image NR
    end_obj = int(pageid) * results_per_page # end with image NR
    if end_obj > rez_obj.count(): # if end NR exceeds limit set it to end NR
        end_obj = rez_obj.count()

    args['paginator'] = Paginator( pagecount, pageid, 10 )
    args['temas'] = rez_obj[start_obj:end_obj]

    response = render(request, 'theme.html', args)
    response.set_cookie( key='page_loc', value='/idea/page=' + str(pageid) + '/' )
    return response


# ================================================================================
# SUPER TEMAS (Izvele pa kategorijam)
def super(request, s_id, pageid=1):
    args = create_args(request)
    if args['username'].get_username() == '': # NO USER
        return redirect('access_denied')
    else:
        garden_access = User_data.objects.get(user_user = args['username']).idea
    if garden_access != True:
      # ACCESS DENIED
        return redirect('access_denied')

    try:
        args['garden_add'] = User_data.objects.get(user_user = args['username']).idea_add
    except:
        pass

    try:
        s = SuperTheme.objects.get(slug=str(s_id))
    except:
        return redirect('/idea/')

    args['super'] = SuperTheme.objects.all().order_by('order')
    args['user'] = auth.get_user(request)

    args['title'] = u'Ideju Lāde | ' + s.title
    args['heading'] = u'Ideju Lāde'
    args['active_tab'] = s.slug

    args['disable_back'] = True

    rez_obj = Theme.objects.filter( relate_to_super = s, parent = None ).order_by('comment', '-last_entry')

    results_per_page = 3

    if int(pageid) < 1: # negative page number --> 404
        return redirect ('/idea/')

    pagecount = int(math.ceil( int(rez_obj.count()) / float( results_per_page ))) # integer identical to range by count

    if int(pageid) > pagecount: # pageid exceeds pagecount --> 404
        return redirect ('/idea/')

    start_obj = int(pageid) * results_per_page - results_per_page # start from image NR
    end_obj = int(pageid) * results_per_page # end with image NR
    if end_obj > rez_obj.count(): # if end NR exceeds limit set it to end NR
        end_obj = rez_obj.count()

    args['paginator'] = Paginator( pagecount, pageid, 10 )
    args['temas'] = rez_obj[start_obj:end_obj]

    args['add_tema'] = True
    args['form'] = ThemeForm

    response = render(request, 'theme.html', args)
    response.set_cookie( key='page_loc', value='/idea/' + str(s_id) + '/' )
    return response
