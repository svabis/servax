#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image, ImageDraw
from time import sleep as pauze
from random import randint as rnd
from datetime import datetime, timedelta

import threading

# SEARCH FOR LIFE FORMS
def chk_around(x, y, sim):
    try:
        if int(img[x][y]) == int(sim):
            return 1
        elif int(img[x][y]) != 0:
            return 2
        else:
            return 3
    except:
        return 0
# 0 - coords dont exist
# 1 - sim found
# 2 - other life found
# 3 - no life found


# CHECK COORDINATES
def chk_coord(x, y):
    if int( img[x][y] ) != 0:
        sim = int(img[x][y])
    else:
        return False

    sim_count = 0
    oth_count = 0
    not_count = 0

    for coords in c_around:
        temp = chk_around( x + coords[0], y + coords[1], sim )
        if temp == 3:
            not_count += 1
        elif temp == 2:
            oth_count += 1
        elif temp == 1:
            sim_count += 1

   # Total life count
    tot_count = sim_count + oth_count

   # OVERPOPULATED --> EXTINCT --> EXIT
    if sim_count == 8:
        img[x][y] = 0
        print_there(x, y, 0)
       # EXTINGUISH LIFE FORM NEXT TO IT...
        planted = False
        while planted != True:
            temp = rnd(0, 7)
            if chk_around( x + c_around[temp][0], y + c_around[temp][1], sim) == 1:
                planted = True
                img[ x + c_around[temp][0] ][ y + c_around[temp][1] ] = 0
                print_there( x + c_around[temp][0], y + c_around[temp][1], 0 )
        return True

    ret = False

   # SMALL AMOUNT OF ENEMIES --> KILL ENEMY
    if 1 <= oth_count <= 2:
        planted = False
        for _ in range(0, ext):
            while planted != True:
                temp = rnd(0, 7)
                if chk_around( x + c_around[temp][0], y + c_around[temp][1], sim) == 2:
                    planted = True
                    temp_sim = int(img[ x + c_around[temp][0] ][ y + c_around[temp][1] ])
                    if temp_sim < sim and ((temp_sim % 2 == 0 and sim % 2 == 0) or (temp_sim % 2 != 0 and sim % 2 != 0)):
                        img[ x + c_around[temp][0] ][ y + c_around[temp][1] ] = sim
                        print_there( x + c_around[temp][0], y + c_around[temp][1], int(sim)-1 )
                        ret = True
#                    return

   # LARGE AMOUNT OF ENEMIES --> KILL SIM
    if 6 <= oth_count <= 8:
        planted = False
        while planted != True:
            temp = rnd(0, 7)
            if chk_around( x + c_around[temp][0], y + c_around[temp][1], sim) == 2:
                planted = True
                temp_sim = int(img[ x + c_around[temp][0] ][ y + c_around[temp][1] ])
                if sim < temp_sim and ((temp_sim % 2 == 0 and sim % 2 == 0) or (temp_sim % 2 != 0 and sim % 2 != 0)):
                    img[x][y] = temp_sim
                    print_there( x, y, temp_sim-1 )
                    ret = True
#                return

   # FREE SPACE --> ADD SIM
    if not_count > 3:
        planted = False
        while planted != True:
            temp = rnd(0, 7)
            if chk_around( x + c_around[temp][0], y + c_around[temp][1], sim) == 3:
                img[ x + c_around[temp][0] ][ y + c_around[temp][1] ] = sim
                planted = True
                print_there( x + c_around[temp][0], y + c_around[temp][1], int(sim)-1 )
                ret = True
#                return

    if ret == True:
        return True
    return False

# Draw output at coordinates
def print_there(x, y, sim):
    draw = ImageDraw.Draw(image)
    if sim == 0:
        draw.rectangle( [y*ratio, x*ratio, y*ratio+ratio, x*ratio+ratio], fill=( (0,0,0) ), outline=0 )
    else:
        draw.rectangle( [y*ratio, x*ratio, y*ratio+ratio, x*ratio+ratio], fill=( s[sim] ), outline=0 )
    del draw

# DISPLAY IMAGE
def display():
#    image.save("/var/www/html/image.jpg", "JPEG")
    image.save("/var/www/svabis.eu/media/stream/life.jpg", "JPEG")


# CREATE LIFE
def create_life():
#    for i in range(1, lf+1):
#        color = 0
#        while color < 100:
#            tempr = rnd(0, 254)
#            tempg = rnd(0, 254)
#            tempb = rnd(0, 254)
#            color = tempr + tempg + tempb

#        s.append( (tempr, tempg, tempb) )

    temp = []
    for n in range(width * height):
        temp.append( rnd(0, r) )

    count = 0
    for j in range(0, height):
        for i in range(0, width):
            if 1 <= temp[count] <= len(s):
                    img[j][i] = temp[count]
            count += 1


# Initial Image output
def draw_all():
    for j in range(0, height):
        for i in range(0, width):
            if int( img[j][i] ) != 0:
                 print_there( j, i, int(img[j][i])-1 )



# MAIN BLOCK
# Coordinates around chosen point
c_around = [[-1, -1], [-1, 0], [-1, +1], [0, -1], [0, +1], [+1, -1], [+1, 0], [+1, +1]]

# SET Image size
width = 900
height = 450
# SET color depth
channels = 3

# SET zoom ratio
ratio = 3

# life form intensity
r = 5000

# "life form" count
#lf = rnd(10, 25)
lf = 4

# Array of colors for life forms
#s = []
#s = [        "green", "blue", "yellow", "red",]
#s = [(0,0,0), (0,250,0), (50,50,200), (200,220,50), (240,15,15),]
s = [(0,0,0), (50,50,200), (200,220,50), (240,15,15),]

# wtf ???
ext = 5

# Create an empty black image
image = Image.new('RGB', [width, height], color=(0, 0, 0))

# Resize width&height to numpy array size
width = int( width / ratio )
height = int( height / ratio )

# Create numpy array
img = np.zeros((height, width))

display()
#pauze(5)

# CREATE LIFE
create_life()

print(len(s))
draw_all()
display()
pauze(2)

# LET's LIVE
array = int(height * width / 20 * 16.15)


# each lifeform separate
def live(sim):
    while True:
        if sim == 0:
            coord_array = np.argwhere(img != 0)
        else:
            coord_array = np.argwhere(img == sim)

        activity = False

#        ex_c = 0
        while activity != True:

            temp = rnd(0, len(coord_array)-1)

            x = coord_array[temp][0]
            y = coord_array[temp][1]

            activity = chk_coord( x, y )

           # escape if array is filled
#            if activity != True:
#                ex_c += 1
#            if ex_c > 3000:
#                activity = True
#                print( "X" )

# program will wait for thread to finish
# l = threading.Thread(target=live, args=())
# program will kill thread on exit

def main_life():
  l0 = threading.Thread(target=live, args=( 0, ), daemon=True)
  l0.start()
  #l1 = threading.Thread(target=live, args=( rnd(1,lf) ,), daemon=True)
  #l1.start()

  lo = threading.Thread(target=live, args=( 1, ), daemon=True)
  lo.start()
  #le = threading.Thread(target=live, args=( 2, ), daemon=True)
  #le.start()


  def all():
    for i in range(1, lf+1):
        l = threading.Thread(target=live, args=(i,), daemon=True)
        l.start()
  #all()

  end_simulation = datetime.now() + timedelta(minutes=5)
  print( datetime.now() )
  print( end_simulation )


# DISPLAY LOOP UNTIL END TIME
  while datetime.now() < end_simulation:
#      draw_all()
      display()
      pauze(1)

  print( "--- EXITED ---" )
  print( end_simulation )
  print( datetime.now() )
