# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.

# 把商品列表goodsinfo做为内嵌表
class goodsinfoLine(admin.StackedInline):#不用tableinline，表格行记录不好写
    model = goodsinfo
    extra = 1#默认内嵌的条数设为1



#把图片列表做为商品的内嵌表
class goodsimagesLine(admin.TabularInline):
    model = goodsimages
    extra=1


# 把规格尺寸列表做为商品的内嵌表
class sizeLine(admin.StackedInline):
    model = size
    extra = 1
# # 把促销活动列表做为商品管理的内嵌表
# class salesgoodsLine(admin.StackedInline):
#     model = salesgoods
#     extra = 1

#装饰器 注册方式
# 商品类型
@admin.register(goodstype)
# goodstype的管理模块
class goodstypeAdmin(admin.ModelAdmin):
    list_display = ['gtitle', 'gcontext','gtfk', 'ctime', 'utime', 'is_Delete']  # 显示的字段
    list_filter = ['gtitle',]  # 过滤器类型名和父类
    search_fields = ['gtitle','gtfk__gtitle']  # 使用类型名和父类两个字段进行搜索，可以模糊匹配
    list_per_page = 1  # 分页 ，1页1条
    # inlines = [goodsinfoLine]



#器型
@admin.register(qixing)
class qixingAdmin(admin.ModelAdmin):
    list_display = ['qtitle']  # 显示的字段
    list_filter = ['qtitle', ]  #
    search_fields = ['gititle']  # 搜索器
    list_per_page = 1  # 分页 ，1页1条
    # inlines = [sizeLine]#内嵌规格尺寸表，既然在商品中嵌入了，就不要在这里嵌入。


#器型规格尺寸
@admin.register(size)
class sizeAdmin(admin.ModelAdmin):
    list_display = ['sqixing', 'w', 'd', 'h', 'unti', 'oldsize', 'oldunti','sprice']  # 显示的字段
    list_filter = ['sqixing', ]  # 过滤器制造商名称
    search_fields = ['sqixing']  # 搜索器
    list_per_page = 1  # 分页 ，1页1条

#包装
@admin.register(packaging)
class packagingAdmin(admin.ModelAdmin):
    list_display = ['pmateria', 'pw', 'pd', 'ph', 'punti', 'ppic']  # 显示的字段
    list_filter = ['pmateria', ]  #
    search_fields = ['pmateria']  # 搜索器
    list_per_page = 1  # 分页 ，1页1条

#服务
@admin.register(server)
class serverAdmin(admin.ModelAdmin):
    list_display = ['stitle', 'sico', 'scont']  # 显示的字段
    list_filter = ['stitle', ]  #
    search_fields = ['stitle']  # 搜索器
    list_per_page = 1  # 分页 ，1页1条

#商品图片列表
@admin.register(goodsimages)
class goodsimagesAdmin(admin.ModelAdmin):
    list_display = ['gimgoods', 'gpic', 'gpd', 'gph', 'gppoint']  # 显示的字段
    list_filter = ['gimgoods', ]  #
    search_fields = ['gimgoods']  # 搜索器
    list_per_page = 1  # 分页 ，1页1条

# 商品
@admin.register(goodsinfo)
class goodsinfoAdmin(admin.ModelAdmin):
    list_display = ['pk','gtitle', 'gmaterials', 'gtechnique', 'gmax','gsynopsis','gpack',
                    'ctime','utime','gsupplier']  # 列表显示的字段
    list_filter = ['gsupplier__sname', ]  # 过滤器制造商名称
    search_fields = ['gititle', 'gqixing','gsupplier__sname','gsynopsis','gxprice','goodstype' ]  # 搜索器
    list_per_page = 1  # 分页 ，1页1条
    filter_horizontal = ('gserver','goodstype')#filter_horizontal 是多对多字段使用的选择器
    inlines = [sizeLine,goodsimagesLine]#
    fields = ['gsupplier','gtitle', ('gmaterials', 'gtechnique','gpack', 'gmax'),'gsynopsis','gserver','goodstype']
    # exclude = []#在增加和删除页面不显示该字段

# 商品统计
@admin.register(goodscount)
class goodscountAdmin(admin.ModelAdmin):
    list_display = ['id','gclick','gevalu','gorder','gback']
    list_filter = ['gclick','gevalu','gorder','gback']  # 根据在平台中的统计数据进行过滤
    search_fields = ['gclick','gevalu','gorder','gback']


# 促销活动
@admin.register(salesgoods)
class salesgoodsAdmin(admin.ModelAdmin):
    list_display = ['stitle', 'sstart', 'send','sdiscount']
    list_filter = ['stitle',]  # 根据商品在平台中的状态进行过滤
    search_fields = ['stitle', 'sstart', 'send','sdiscount']
# 商品管理
@admin.register(goodsmangent)
class goodsmangentAdmin(admin.ModelAdmin):
    list_display = ['gmgoods','gxprice','gstatus','grecommendation','is_Delete']
    list_filter = ['gstatus','grecommendation']#根据商品在平台中的状态进行过滤
    filter_horizontal = ['gmsales']#选择或添加促销活动
    search_fields = ['gmgoods','gxprice','gstatus','grecommendation','is_Delete']


#创意众筹(管理预售商品)
@admin.register(crfdinfo)
class crfdinfoAdmin(admin.ModelAdmin):
    list_display = ['id','ctarget','cmax','cterm','cstatus','cusernum','cclick','ctime','utime','is_Delete',]
    list_filter = ['cstatus']#根据众筹状态进行过滤
    readonly_fields = ['cusernum','cclick']
