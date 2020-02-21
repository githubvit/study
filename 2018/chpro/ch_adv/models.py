# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ch_supplier.models import *
from ch_goods.models import *
import django.utils.timezone as timezone
# Create your models here.
'''
版面内容管理，网站编辑
'''
# 首页轮播图-品牌或制造商广告 ：回答是哪个制造商或哪个品牌的id下的所有商品
# 首页类别头图-品牌或制造商广告：回答是该类别id下 哪个制造商或哪个品牌的id 下的所有该类别商品
# 首页类别编辑推荐-商品广告：回答是该类别id下 哪个制造商或哪个品牌id 下的商品ID
# 页面、位置、图片大小、图片高度、图片宽度、图片url
# 广告控制程序思路：参数-位置列表
#   选取广告该位置model，id正向排序，也就是先到先发，期初都置为0，上线置为1，记录上线时间，并根据到期数和上线时间计算到期时间，到期置状态置为2。用time.time()比对到期时间。
# 首页广告类型

# 首页位置类型
class adv1type(models.Model):
    advtitle = models.CharField(max_length=32, verbose_name="首页位置名称")
    advposition1 = models.IntegerField(verbose_name="首位")
    advposition2 = models.IntegerField(verbose_name="次位")
    advprice = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="位置单价:RMB/期", default=10000.00)
    ctime = models.DateTimeField(auto_now_add=True,verbose_name="建立时间")
    utime = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    is_Delete = models.BooleanField(default=False, verbose_name="是否发布")
    def __unicode__(self):
        return "%s:位置%s"%(self.advtitle,self.advposition2)
    class Meta:
        verbose_name = '首页位置'  # 改对象名
        verbose_name_plural = "首页位置列表"  # 改表名

#首页 广告规格

# 首页位置内容
class adv1(models.Model):
    advtp=models.ForeignKey(adv1type,verbose_name="首页位置",related_name="adv_1")
    advpic1 = models.ImageField(upload_to='adv_goods', verbose_name='首页跳转图片',null=True,blank=True)
    advpic1art = models.CharField(max_length=16, verbose_name='首页跳转图片提示',null=True,blank=True)
    advpic2 = models.ImageField(upload_to='adv_goods', verbose_name='次页图片',null=True,blank=True,help_text="图片大小不超过200kb，高360px，宽1090px")
    advpic2art = models.CharField(max_length=16, verbose_name='次页图片提示',null=True,blank=True)
    advnum=models.IntegerField( verbose_name="位置期数",help_text="每期30天",default=1)
    advgt= models.ForeignKey(goodstype, verbose_name="类别",null=True,blank=True,related_name="adv_1")
    advgoods= models.ForeignKey(goodsmangent, verbose_name="商品",null=True,blank=True,related_name="adv_1")
    ctime = models.DateTimeField(auto_now_add=True, verbose_name="建立时间")
    utime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    advuser = models.ForeignKey(SupplierInfo, verbose_name="内容发布人",default='',blank=True,related_name="adv_1")#(开发阶段设置可以为空，但实际不能这样设，必须要有发布人，因为这是要传递的参数)
    advstatus_choice=(
        (0,u'预备'),
        (1,u'上线'),
        (2,u'到期下线'),
    )
    advstatus=models.IntegerField(choices=advstatus_choice,default=0,verbose_name="版面状态")
    is_Delete=models.BooleanField(default=False,verbose_name="是否发布")
    def __unicode__(self):
        return "%s:位置%s"%(self.advuser,self.advtp)
    class Meta:
        verbose_name = '首页位置内容'  # 改对象名
        verbose_name_plural = "首页位置内容列表"  # 改表名

# 广告投放
# class advgo(models.Model):
#     advuser=models.ForeignKey(SupplierInfo,verbose_name="投放人",null=True,blank=True)
#     advbrand=models.ForeignKey(brand,verbose_name="投放品牌",null=True,blank=True)

# 编辑推荐
# 买手(《访瓷》)