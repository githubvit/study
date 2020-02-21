# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
from ch_goods.admin import goodsinfoLine
# Register your models here.
# 制造商账号
@admin.register(suser)
class suserAdmin(admin.ModelAdmin):
    pass


# 制造商
@admin.register(SupplierInfo)
class SupplierInfoAdmin(admin.ModelAdmin):
    list_display = ['sname', 'stype','spuser','ssynopsis','saddress','saccount','sphon','scontact', 'ctime']  # 显示的字段
    list_filter = ['sname','stype','spuser',]  # 过滤器商家名称、类型、账号
    search_fields = ['sname',]  # 搜索器
    list_per_page = 1  # 分页 ，1页1条
    inlines = [goodsinfoLine]