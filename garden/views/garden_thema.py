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
# TEMA
def temas(request, s_id, t_id, pageid=1):
    try:
        t = Theme.objects.get(slug=str(t_id))
    except:
        return redirect ('/garden/')

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

    args['heading'] = u'Dārzs | ' + t.relate_to_super.title + " | " + t.title
    args['active_tab'] = t.relate_to_super.slug

    args['parent'] = t.parent
    args['s_id'] = str(s_id)

   # IF TEMA COMMENT IS DISABLED
    if t.comment == False:
        temas = Theme.objects.filter( parent = t ).order_by('comment', '-last_entry')

        args['temas'] = temas
        args['add_tema'] = True

        args['form'] = ThemeForm

        response = render(request, 'theme.html', args)
        response.set_cookie( key='page_loc', value='/garden/' + str(s_id) + '/' + str(t_id) + '/' + str(pageid) + '/' )
        return response

    args['tema_nr'] = t.id
    args['tema_slug'] = t.slug
    args['tema_title'] = t.title

    results_per_page = 50

    rez_obj = Post.objects.filter(relate_to = t).order_by('date')

    if int(pageid) < 1: # negative page number --> 404
        return redirect ('/')

    pagecount = int(math.ceil( int(rez_obj.count()) / float( results_per_page ))) # integer identical to range by count

    if int(pageid) > pagecount and int(pageid) > 1: # pageid exceeds pagecount --> 404
        return redirect ('/')

    start_obj = int(pageid) * results_per_page - results_per_page # start from image NR
    end_obj = int(pageid) * results_per_page # end with image NR
    if end_obj > rez_obj.count(): # if end NR exceeds limit set it to end NR
        end_obj = rez_obj.count()

    args['paginator'] = Paginator( pagecount, pageid )
    args['diskusija'] = rez_obj[start_obj:end_obj]

    args['form'] = PostForm

    if request.POST:
        form = PostForm( request.POST, request.FILES )

        if form.is_valid():
            new_coment = form.save( commit = False )
            new_coment.relate_to = t
            new_coment.user = args['user']
            new_coment.save()

            while t.parent != None:
                try:
                    t.parent.last_entry = new_coment.date
                    t.parent.save()
                except:
                    pass
                t.last_entry = new_coment.date
                t.entry_count += 1
                t.save()
                t = t.parent

            response = redirect( '/garden/' + str(s_id) + '/' + str(t_id) + '/#new_comment' )
            response.set_cookie( key='page_loc', value='/garden/' + str(s_id) + '/' + str(t_id) + '/#new_comment' )
            return response
    else:
        args['form'] = PostForm

    response = render(request, 'discussions.html', args)
    response.set_cookie( key='page_loc', value='/garden/' + str(s_id) + '/' + str(t_id) + '/' + str(pageid) + '/' )
    return response
