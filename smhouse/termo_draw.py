# -*- coding: utf-8 -*-
from django.db.models import Max, Min
from django.conf import settings

from smhouse.models import TermoAdress, TermoPlace, TermoReading

from datetime import datetime, timedelta

from PIL import Image, ImageDraw, ImageFont

import os

def draw_termo(slug, day_h, step_h, fmt, x_s, ambient):
   # output image parameters
    w_h, tab, ax_col, gr_col = [1520, 400], 50, "#333", "#aaa"
   # TermoAdress
    termo = TermoAdress.objects.get(slug = slug)

  # TermoPlaces Reading's select
    if ambient is not None:
        tp = TermoPlace.objects.filter( where = termo, ambient = ambient )
        data = "temp"
    else:
        tp = TermoPlace.objects.filter( where = termo )
        data = "humy"

   # get Dateime range & array for x-axis (full hours)
    d_start, d_end = datetime.now() - timedelta(hours=day_h), datetime.now()

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
    draw.line([tab, 10, tab, 370], fill=ax_col, width = 0)
    draw.line([tab, 370, 1490, 370], fill=ax_col, width = 0)

   # draw hours
    for h in hours:
        x = int( round(( h.timestamp() - d_start.timestamp() )/(day_h/24))/60 ) + tab
        draw.line([x, 10, x, 370], fill=gr_col, width = 0)
        draw.text([x-4, 375], h.strftime(fmt), fill=(0,0,0,128))

   # Format y-axis
    min, max = 60, -20
    for t in tp:
        temp = TermoReading.objects.filter(place = t, date__range=[d_start, d_end])

        t_max = temp.aggregate(Max( data ))
        try:
            if float(t_max[ data + '__max']) >= max:
                max = float(t_max[ data + '__max'])
        except:
            pass

        t_min = temp.aggregate(Min( data ))
        try:
            if float(t_min[ data + '__min']) <= min:
                min = float(t_min[ data + '__min'])
        except:
            pass

    y_k = -300/(max - min)

   # Draw y-axis legend
    draw.line([tab, ((max-min)*y_k)+350, 1490, ((max-min)*y_k)+350], fill="#A52A2A", width = 0)
    draw.text([10,  ((max-min)*y_k)+345], str(max), fill=(165,42,42,128))

    draw.line([tab, ((min-min)*y_k)+350, 1490, ((min-min)*y_k)+350], fill="#2a55a5", width = 0)
    draw.text([10,  ((min-min)*y_k)+345], str(min), fill=(42,85,165,128))

    for i in range(1, 5):
        draw.line([tab, ((max-min)*y_k*0.2*i)+350, 1490, ((max-min)*y_k*0.2*i)+350], fill=gr_col, width = 0)
        draw.text([10,  ((max-min)*y_k*0.2*i)+345], str(round( ((max-min)*0.2*i)+min, 1 )), fill=(0,0,0,128))

    img.save( settings.MEDIA_ROOT + 'smhouse/termo/' + slug + '_' + str(day_h) + '_back_' + str(ambient) + '.png' )

   # iterate Graph's
    for t in tp:
       # TermoReaings
        tr = TermoReading.objects.filter(place=t, date__range=[d_start, d_end]).order_by('-date')

       # layer with Transparent backgroung
        img = Image.new('RGBA', w_h, (255, 0, 0, 0))
        draw = ImageDraw.Draw( img )

       # plot reaings data
        for r in tr:
            x = int( round(( r.date.timestamp() - d_start.timestamp() )/(day_h/24)/60 )) + tab
            if ambient is not None:
               # temperature output
                y = int((float(r.temp) - min) * y_k) + 350
            else:
               # humidity
                try:
                    y = int((float(r.humy) - min) * y_k) + 350
                except:
                   # humidity is None
                    y = int((float(120) - min) * y_k) + 350

            draw.rectangle( [x, y, x+2, y+2], fill=t.color, outline=t.color, width=4 )

       # save image
        if ambient is not None:
            img.save( settings.MEDIA_ROOT + 'smhouse/termo/' + t.where.slug + '_' + str(day_h) + '_temp_' + str(t.order) + '.png', 'PNG' )
        else:
            img.save( settings.MEDIA_ROOT + 'smhouse/termo/' + t.where.slug + '_' + str(day_h) + '_humy_' + str(t.order) + '.png', 'PNG' )
