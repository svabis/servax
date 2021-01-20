# -*- coding: utf-8 -*-
import math     # for rounding up Page Counter

class Paginator(object):
    visible = True  # PAGINATOR ON/OFF
    big = True      # <<<< / >>>> ON/OFF
    pages = []
    active_page = 1
    pagecount = 1

# ARRAY 9 ELEMENTS
#                                     x
#EX: 1,  2, ..., ..., ..., ...,  13, 14, 15
#                     x
#EX: 1,  2, ..., 5,   6,   7,   ..., 14, 15
#        x
#EX: 1,  2,   3, ..., ..., ..., ..., 14, 15

#EX: 1,  2,  3,  4,  5,  6,  7,  8,  9		 9 PAGES OR LESS
#EX: 1,  2,  3,  4,  5,  6, ..,  9, 10		10 PAGES
#EX: 1,  2, ..,  5,  6,  7, .., 10, 11		11 PAGES OR MORE


# CONSTRUCTOR
    def __init__(self, count, current, pc ):
        self.active_page = int(current)
        self.pagecount = count
        self.pages = []
#        pc = 5
        pch = int(pc/2)

       # IF PAGE IS ONE => PAGINATOR HIDEN
        if count < 2:
            self.visible = False
        else:
            self.visible = True

       # NO "GAP'S"
        if count < pc:
            self.big = False
            for nr in range(count):
                self.pages.append( nr + 1 )
       # ONE OR TWO "GAP'S"
        else:
           # "GAP" IN THE END
            if int(current) < pch:
                for nr in range(pch):
                    self.pages.append( nr + 1 )
                self.pages.append( 0 )
                self.pages.append( count-1 )
                self.pages.append( count )

           # "GAP" IN THE BEGINING
            elif int(current) > (count-pch):
                self.pages.append( 1 )
                self.pages.append( 2 )
                self.pages.append( 0 )
                for nr in range(count-pch, count):
                    self.pages.append( nr + 1 )

           # TWO "GAP'S"
            else:
                self.pages.append( 1 )
                if pc > 6:
                    self.pages.append( 2 )
                self.pages.append( 0 )		# GAP
                if pc > 6:
                    self.pages.append( int(current) - 1 )
                self.pages.append( int(current) )
                if pc > 6:
                    self.pages.append( int(current) + 1 )
                self.pages.append( 0 )		# GAP
                if pc > 6:
                    self.pages.append( count-1 )
                self.pages.append( count )

# piemēram ja ir tikai viena tad lapu dalītāja nav vispār	# DONE !!!
# ja ir līdz 10 -> sānu pogas nav un visur ir cipari		# DONE !!!
# ja  10 ... 13 tad viens "robs"
# ja vairāk -> viens "robs" ja galā, divi "robi" ja pa vidu...
