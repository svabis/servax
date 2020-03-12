# -*- coding: utf-8 -*-
from django.urls import path

from garden.views import main, temas, super, add_tema, del_post


urlpatterns = [
# del_post
    path('del_post/<int:p_id>/', del_post),

# ADD TEMA
    path('add_tema/', add_tema),

# temas diskusijas + add Ieraksts --- DJANGO 2
    path('<str:s_id>/<str:t_id>/<int:pageid>/', temas),
    path('<str:s_id>/<str:t_id>/', temas),

# SuperTema izvele
    path('<str:s_id>/<int:pageid>/', super),
    path('<str:s_id>/', super),

# MAIN --> Visas Tema ar comment=True
    path('', main),
]
