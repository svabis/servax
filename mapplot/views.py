# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from django.contrib import auth

from login.models import User_data

from .models import MapPlot, MapPlotCity
from .forms import MapPlotForm

from main.args import create_args


# !!!!! MAPPLOT MAIN & ADD NEW !!!!!
def plot(request):
    args = create_args(request)
    args['title'] = 'Kartes plotteris | Svabwilla'
    args['heading'] = 'Kartes ploteris'

    args['data'] = MapPlot.objects.filter( deleted=False)

    args['form'] = MapPlotForm

    if request.POST: # actions if login Form is submitted
        form = MapPlotForm( request.POST )
        if form.is_valid():
            form.save()

# !!!!!!!!!!!!!!!!!!!!!!!
# !!!!! Validate ID !!!!!
# !!!!!!!!!!!!!!!!!!!!!!!

           # Set return to added Point
            c = request.POST['zoom']
            response = redirect( '/mapplot/plot/')
            response.set_cookie( key='view', value=c, path='/', max_age=5 )
#            response.set_cookie( key='city', value=request.POST['city'], path='/') #, max_age=5 )
            return response

        else:
# !!!!! TE IF IR ERRORS FORMAI
            pass


    response = render(request, 'plot.html', args)
    response.set_cookie( key='page_loc', value='/plot/', path='/' )
    return response



# ==================================================================================================================================================
# !!!!! MAPPLOT MAIN & ADD NEW !!!!!
def plot_edit(request, e_id):
    args = create_args(request)
    args['title'] = 'Kartes plotteris | Svabwilla'
    args['heading'] = 'Kartes ploteris'

#    args['data'] = MapPlot.objects.all()
    args['data'] = MapPlot.objects.filter(id=e_id)

    edit = MapPlot.objects.get( id=e_id )
    args['edit'] = edit

    args['form'] = MapPlotForm( instance=edit )

    if request.POST: # actions if login Form is submitted
        form = MapPlotForm( request.POST, instance=edit )
        if form.is_valid():
            form.save()

# !!!!!!!!!!!!!!!!!!!!!!!
# !!!!! Validate ID !!!!!
# !!!!!!!!!!!!!!!!!!!!!!!

           # Set return to added Point
            c = request.POST['zoom']
            response = redirect( '/mapplot/plot/')
            response.set_cookie( key='view', value=c, path='/', max_age=5 )
#            response.set_cookie( key='city', value=request.POST['city'], path='/') #, max_age=5 )
            return response

        else:
# !!!!! TE IF IR ERRORS FORMAI
            pass


    response = render(request, 'plot.html', args)
    response.set_cookie( key='page_loc', value='/plot/', path='/' )
    return response




# ==================================================================================================================================================
# !!!!! MAPPLOT DELETE !!!!!
def plot_del(request, d_id):
    args = create_args(request)
#    args['title'] = 'Kartes plotteris | Svabwilla'

    plot = MapPlot.objects.get( id=d_id )
    plot.deleted = True
    plot.save()

   # Set return to added Point
    c = plot.lat + ":" + plot.lon + ":" + "18"
    response = redirect( '/mapplot/plot/')
    response.set_cookie( key='view', value=c, path='/', max_age=5 )
#            response.set_cookie( key='city', value=request.POST['city'], path='/') #, max_age=5 )
    return response
