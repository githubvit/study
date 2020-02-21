# -*- coding: utf-8 -*-
from django.conf.urls import url
import views
from wxlogin import wxlogin
urlpatterns = [
    url(r'^$',views.user, name='user'),
    url(r'^register_exist/$',views.register_exist, name='register_exist'),
    url(r'^registerhandle/$',views.registerhandle, name='registerhandle'),
    url(r'^checkcode/', views.CheckCode, name='checkcode'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^logistics/', views.logistics, name='logistics'),
    url(r'^lg_del/', views.lg_del, name='lg_del'),
    url(r'^chang_upwd/', views.change_upwd, name='chang_upwd'),
    url(r'^login_wx/$', views.login_wx, name='login_wx'),
    url(r'^polling_wx/$', views.login_wx, name='polling_wx'),

]