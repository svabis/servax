# -*- coding: utf-8 -*-
from django.db.models import Max, Min
from django.conf import settings

from django.utils.timezone import make_aware

from smhouse.models import Location, TermoPlace, TermoReading

from datetime import datetime, timedelta

from PIL import Image, ImageDraw, ImageFont

import os

import math



def draw_termo(slug, day_h, step_h, fmt, x_s, name, ambient):
   # output image parameters
    gh, w_h, g_wh = 420, [1520, 450], [40,1480]
    ax_col, gr_col = "#333", "#aaa"
    txtp = [10, 1495]
    minmax_txt_loc = [ 50, 150, 250, 350, 450, 550, 650 ]


   # TermoAdress
    termo = Location.objects.get(slug = slug)

  # TermoPlaces Reading's select
    if ambient is not None:
        tp = TermoPlace.objects.filter( where = termo, ambient = ambient )
        data = "temp"
    else:
        tp = TermoPlace.objects.filter( where = termo )
        data = "humy"

    if tp.count() == 0:
        return False

   # get Dateime range & array for x-axis (full hours)
    d_start, d_end = make_aware(datetime.now() - timedelta(hours=day_h)), make_aware(datetime.now())

   # Start Hour
    if x_s == 1:
        prev = d_end.replace(microsecond=0, second=0, minute=0)
   # Start Day
    if x_s == 2:
        prev = d_end.replace(hour=0, microsecond=0, second=0, minute=0)
   # Start First Day of month
    if x_s == 3:
        prev = d_end.replace(day=1, hour=0, microsecond=0, second=0, minute=0)

    next = d_start.replace(microsecond=0, second=0, minute=0)

    hours = [prev]
    while hours[-1] > next:
        prev = prev - timedelta(hours=day_h/step_h)
        hours.append( prev )

    if d_start > hours[-1]:
        hours.pop()

   # BACKGROUND IMAGE
    img = Image.new('RGB', w_h, color = '#cecff0')
    draw = ImageDraw.Draw( img )

   # draw hours
    for h in hours:
        x = int( round(( h.timestamp() - d_start.timestamp() )/(day_h/24))/60 ) + g_wh[0]
        draw.line([x, g_wh[0]+20, x, gh], fill=gr_col, width = 0)
        draw.text([x-4, gh+5], h.strftime(fmt), fill=(0,0,0,128))

   # draw axis
    draw.line([g_wh[0], g_wh[0], g_wh[0], gh], fill=ax_col, width = 0)
    draw.line([g_wh[1], g_wh[0], g_wh[1], gh], fill=ax_col, width = 0)
    draw.line([g_wh[0], gh,      g_wh[1], gh], fill=ax_col, width = 0)

   # Format y-axis
    min, max = 60, -20
    for t in tp:
        temp = TermoReading.objects.filter(place = t, date__range=[d_start, d_end])

        t_max = temp.aggregate(Max( data ))
        try:
            if float(t_max[ data + '__max']) >= max:
                max = math.ceil( float(t_max[ data + '__max']) )
                max_old = int( t_max[ data + '__max'] )
        except:
            pass

        t_min = temp.aggregate(Min( data ))
        try:
            if float(t_min[ data + '__min']) <= min:
                min = math.floor( float(t_min[ data + '__min']) )
        except:
            pass

    y_k = -350/(max - min)


   # IF NO DATA IN THIS PERIOD --> don't draw y axis
    if max != -20 and min != 60:

       # Draw y-axis legend
       # max 'C
        draw.line([g_wh[0], ((max-min)*y_k)+gh, g_wh[1], ((max-min)*y_k)+gh], fill="#A52A2A", width = 0)
        draw.text([txtp[0], ((max-min)*y_k)+gh-5], str(max), fill=(165,42,42,128))
        draw.text([txtp[1], ((max-min)*y_k)+gh-5], str(max), fill=(165,42,42,128))

       # min 'C
#        draw.line([g_wh[0], ((max_old-min)*y_k)+gh, g_wh[1], ((max_old-min)*y_k)+gh], fill="#2a55a5", width = 0)
        draw.text([txtp[0], ((min-min)*y_k)+gh-5], str(min), fill=(0,0,0,128))
        draw.text([txtp[1], ((min-min)*y_k)+gh-5], str(min), fill=(0,0,0,128))

       # calculate y-axis step
        step = [1,  1,2,2,5,5,  5,5,10,10,10,  10,10,10,10,10,  10,10,20,20,20 ]
        amp = round( float((max-min) /5) )

       # calculated 'C
        for t in range(-50, 100, step[amp]):
            c = ((t-min)*y_k)+gh
#            if g_wh[0] < c < gh:
            if 70 < c < gh:
                draw.line([g_wh[0], c, g_wh[1], c], fill=gr_col, width = 0)
                draw.text([txtp[0], c-5], str(t), fill=(0,0,0,128))
                draw.text([txtp[1], c-5], str(t), fill=(0,0,0,128))

       # 0'C
        zero = ((0-min)*y_k)+gh
        if g_wh[0] < zero < gh:
            draw.line([g_wh[0], zero, g_wh[1], zero], fill="#2a55a5", width = 0)
            draw.text([txtp[0], zero-5], "0", fill=(42,85,165,128))
            draw.text([txtp[1], zero-5], "0", fill=(42,85,165,128))

    img.save( settings.MEDIA_ROOT + 'smhouse/termo/' + slug + '_' + name + '_back_' + str(ambient) + '.png' )


   # iterate Graph's
    for i, t in enumerate( tp ):
       # TermoReaings
        tr = TermoReading.objects.filter(place=t, date__range=[d_start, d_end]).order_by('date')

       # layer with Transparent backgroung
        img = Image.new('RGBA', w_h, (255, 0, 0, 0))
        draw = ImageDraw.Draw( img )

       # min max
        obj_max = tr.aggregate(Max( data ))
        obj_min = tr.aggregate(Min( data ))

#        print( obj_max )
#        print( type(obj_max) )
#        print( obj_max.keys() )

#        font = ImageFont.truetype("/var/www/svabis.eu/static/Debrosee-ALPnL.ttf", 10)
        font = ImageFont.truetype("/var/www/svabis.eu/static/Nasa21-l23X.ttf", 16)

        if obj_max.get(data+"__max") is not None:
            draw.text([minmax_txt_loc[i],10], "MAX " + str( obj_max.get(data+"__max") ), fill=t.color, font=font)
        if obj_min.get(data+"__min") is not None:
            draw.text([minmax_txt_loc[i],28], "MIN " + str( obj_min.get(data+"__min") ), fill=t.color, font=font)

       # last temperature
        l_temp = None
       # plot reaings data
        for r in tr:
            x = int( round(( r.date.timestamp() - d_start.timestamp() )/(day_h/24)/60 )) + g_wh[0]
            if ambient is not None:
               # temperature output
                try:
                    y = int((float(r.temp) - min) * y_k) + gh
                except:
                    y = None
#                    pass
            else:
               # humidity
                try:
                    y = int((float(r.humy) - min) * y_k) + gh
                except:
                   # humidity is None
                    y = int((float(120) - min) * y_k) + gh

           # NO VERTICAL DATA
            if y is not None:
              l_temp = r.temp
              if x_s == 1:
                draw.rectangle( [x, y, x+2, y+2], fill=t.color, outline=t.color, width=4 )
              elif x_s == 2:
                draw.rectangle( [x, y, x+1, y+1], fill=t.color, outline=t.color, width=4 )
              else:
                draw.rectangle( [x, y, x,   y],   fill=t.color, outline=t.color, width=4 )

# LAST DATA
        if l_temp is not None: # and ambient is not None:
#        if True:
            draw.text([minmax_txt_loc[i],46], "LAST " + str( l_temp ), fill=t.color, font=font)

       # save image
        if ambient is not None:
            img.save( settings.MEDIA_ROOT + 'smhouse/termo/' + t.where.slug + '_' + name + '_temp_' + str(t.order) + '.png', 'PNG' )
        else:
            img.save( settings.MEDIA_ROOT + 'smhouse/termo/' + t.where.slug + '_' + name + '_humy_' + str(t.order) + '.png', 'PNG' )

    return True

#draw_termo("rpz", 24, 24, "%H", 1, "day", True)
#draw_termo("rpz", 168, 7, "%d", 2, "week", True)
