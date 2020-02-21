# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import *
# 把LogisticsInfo做为内嵌表
class LogisticsInfoLine(admin.TabularInline):
    model = LogisticsInfo
    extra = 1#默认内嵌的条数设为1

#用户表 装饰器 注册方式
@admin.register(UserInfo)
# UserInfo的管理模块
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['uname','uphon','uemail','uctime','is_Delete']#显示的字段
    list_filter = ['uctime']#过滤器用创建时间，可以看出某个时间注册的用户
    search_fields = ['uname','uemail']#使用两个字段进行搜索，可以模糊匹配
    list_per_page = 1 #分页 ，1页1条
    # fieldsets = [ #增加和修改页面的分组
    #     ('必填',{'fields':['uname','uemail']}),
    #     #('选填',{'fields':['uphone']}),#分组不支持有默认值的字段
    #     # ('自动填',{'fields':['uctime']}),#分组不认可以自动创建内容的字段
    # ]
    inlines = [LogisticsInfoLine]#把上面注册的内嵌表导入，因为物流表和用户表时多对一的关系，所以把物流表内嵌到用户表中。
#物流表
@admin.register(LogisticsInfo)
class LogisticsInfoAdmin(admin.ModelAdmin):
    list_display = ['luser','lname','lphon','larea','laddress','lyoubian','lctime','is_Default','is_Delete']
    list_filter = ['luser__uname']#关联字段的过滤，要使用外键字段+双下划线+关联表字段
    search_fields =  ['laddress','luser__uname']#关联字段的搜索，要使用外键字段+双下划线+关联表字段
    list_per_page = 2
#tip1：在admin中通过外键跨表要使用’类‘中外键属性（字段）名+双下划线+关联表字段

# 微信用户信息表
@admin.register(wxuserinfo)
class wxuserinfoAdmin(admin.ModelAdmin):
    list_display = ['wxuin','wxnickname','wxinfo','wxuser','uctime','uuptime']
    list_filter = ['wxnickname']#关联字段的过滤，要使用外键字段+双下划线+关联表字段
    search_fields =  ['wxinfo']#关联字段的搜索，要使用外键字段+双下划线+关联表字段
    list_per_page = 2