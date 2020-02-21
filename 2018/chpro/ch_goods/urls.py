# -*- coding: utf-8 -*-
from django.conf.urls import url
import views
urlpatterns = [

    url(r'^goods/shdz',views.madeorder_handdrawing ,name='shdz'),
    url(r'^goods/zydz',views.madeorder_print ,name='zydz'),
    url(r'^goods/thdz',views.madeorder_paster ,name='thdz'),

]