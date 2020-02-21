# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
# Register your models here.

# 首页位置管理
@admin.register(adv1type)
class adv1typeAdmin(admin.ModelAdmin):
    list_display = ['id','advtitle', 'advposition1','advposition2','advprice','ctime','utime','is_Delete'] # 显示的字段
    # readonly_fields = ['ctime','utime']
    list_filter = ['advtitle',]  # 过滤器制造商名称
    search_fields = ['advtitle', 'advposition1','advposition2','advprice']  # 搜索器
    list_per_page = 10  # 分页 ，1页10条

#首页位置内容
@admin.register(adv1)
class adv1Admin(admin.ModelAdmin):
    list_display = ['id','advtp','ctime','utime','advpic1','advpic1','advnum','advgt','advgoods','advuser','advstatus','is_Delete']
    list_filter = ['advtp','advuser']#根据位置和发布人过滤
    search_fields = ['advtp','advpic1','advpic1','advnum','advgt','advgoods','advuser']  # 搜索器
    list_per_page = 10  # 分页 ，1页10条