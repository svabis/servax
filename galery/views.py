# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect # response to template, redirect to another view

from login.models import User_data # Access data

from galery.models import Galery
from galery.paginator import Paginator  # import paginator

from galery.forms import GaleryAddForm

from main.args import create_args

import math # for rounding up Page Counter

from slugify import slugify


# images on page
img_on_page = 18


# !!!!! Main parameters acces, public e.t.c. !!!!!
def galery_default(request):
    args = create_args(request)
    args['heading'] = "Galerija"
    args['title'] = "Galerija | Svabwilla"

   # IF USER
    if args['username'].get_username() != '':
        galery = User_data.objects.get(user_user = args['username']).galery
        if galery:
           # ACCESS ALL ALOWED
            args['images'] = Galery.objects.all().order_by('-galery_date')
        else:
           # ACCESS PUBLIC IMAGES ONLY
            args['images'] = Galery.objects.filter( galery_public = True ).order_by('-galery_date')

  # nav username
    else:
       # ACCESS PUBLIC IMAGES ONLY
        args['images'] = Galery.objects.filter( galery_public = True ).order_by('-galery_date')

    try:
        args['u_galery_add'] = User_data.objects.get(user_user = args['username']).galery_add
       # Add_image form to template
        if args['u_galery_add']:
            args['form'] = GaleryAddForm
    except:
        args['u_galery_add'] = False

   # Create Tag list
    tags = []
    for g in args['images']:
        tags += g.galery_tags.split(",")
    temp = filter( None, list(set( tags )) )
    tags = []
    for t in temp:
         tags.append( [ slugify(t), t ] )
    args['tag_list'] = tags

    return args


# ============================================================================
# !!!!! BILDES (grid) !!!!!
def galery_main(request, pageid=1):
    args = galery_default(request)
    images = args['images']

    pagecount = int(math.ceil( int(images.count()) / float( img_on_page ))) # integer identical to range by count

    if int(pageid) > pagecount and int(pageid) > 1: # pageid exceeds pagecount
        pageid = pagecount

    start_img = int(pageid) * img_on_page - img_on_page	# start from image NR
    end_img = int(pageid) * img_on_page # end with image NR
    if end_img > images.count(): # if end NR exceeds limit set it to end NR
        end_img = images.count()

    args['images'] = images.order_by('-galery_date')[start_img:end_img] # -argument is for negative sort
    args['paginator'] = Paginator( pagecount, pageid )

    response = render(request, 'galery.html', args)
    response.set_cookie( key='page_loc', value='/galery/' + str(pageid) + '/', path='/' )
    return response


# ============================================================================
# !!!!! BILDES by TAG !!!!!
def galery_tags(request, tag, pageid=1):
    args = galery_default(request)
    temp = args['images']

    tag = str(tag)
   # EMPTY QUERYSET
    images = []

    for b in temp:
        t_array = b.galery_tags.split(",")
        for t in t_array:
            if tag == slugify( t ):
                images.append( b )

    pagecount = int(math.ceil( int( len(images) ) / float( img_on_page ))) # integer identical to range by count

    if int(pageid) > pagecount and int(pageid) > 1: # pageid exceeds pagecount
        pageid = pagecount

    start_img = int(pageid) * img_on_page - img_on_page	# start from image NR
    end_img = int(pageid) * img_on_page # end with image NR
    if end_img > len(images): # if end NR exceeds limit set it to end NR
        end_img = len(images)

    args['images'] = images[start_img:end_img]
    args['paginator'] = Paginator( pagecount, pageid )

    args['tag'] = tag

    response = render(request, 'galery.html', args)
    response.set_cookie( key='page_loc', value='/galery/tag=' + tag + '/' + str(pageid) + '/', path='/' )
    return response


# !!!!! Galery Add !!!!!
def galery_add(request):
    if request.POST:
        form = GaleryAddForm( request.POST, request.FILES )
        form.save()

       # Check ADD FORM...
#        if True:
#        if form.is_valid():
#            temp = Galery(**form.cleaned_data)
#            form.save()

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!! REDIRECT BASED ON COOKIE !!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#            return redirect ('galery_main')

        # !!!!! ERROR WITH POST !!!!!
#        else: # Form not valid...
#            args = {}
#            args['form'] = form
#            args['add_error'] = True
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!! Return BASED ON COOKIE !!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#        return render( 'tren_list.html', args )

#    return True
    return redirect('galery_main')
