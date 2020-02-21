# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#
class suser(models.Model):
    suser = models.CharField(max_length=16, verbose_name='账号',unique=True)
    spwd=models.CharField(max_length=32,verbose_name='密码')
    def __unicode__(self):
        return self.suser
    class Meta:
        verbose_name='商家账号'#改对象名
        verbose_name_plural="商家账号列表"#改表名

class SupplierInfo(models.Model):
    spuser=models.ForeignKey(suser,verbose_name="商家账号",related_name="s_supplier")
    stype_choice=[
        (1,u'个人'),
        (2,u'服务商'),
        (3,u'制造商'),
    ]
    stype=models.IntegerField(choices=stype_choice,verbose_name="商家类型")
    sname=models.CharField(max_length=32,verbose_name='商家名称',unique=True)
    ssynopsis=models.TextField(max_length=128,verbose_name='商家简介')
    saccount=models.CharField(max_length=32,verbose_name='商家财务账号',unique=True)
    saddress = models.CharField(max_length=32, verbose_name='商家地址')
    sphon=models.CharField(max_length=20,verbose_name='商家电话')
    scontact=models.CharField(max_length=20,verbose_name='商家联系人')
    is_Delete = models.BooleanField(default=False, verbose_name='删除')
    ctime = models.DateTimeField(auto_now_add=True, verbose_name="建立时间")
    utime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    def __unicode__(self):
        return self.sname
    class Meta:
        verbose_name='商家'#改对象名
        verbose_name_plural="商家列表"#改表名
# 品牌
class brand(models.Model):
    btitle=models.CharField(max_length=16,unique=True,verbose_name="品牌名称")
    bstory=models.TextField(max_length=128,verbose_name='品牌故事')
    bpic=models.ImageField(upload_to='supplier',verbose_name='宣传图片')
    bsupport=models.ForeignKey(SupplierInfo,verbose_name="所属制造商",related_name="s_brand")
    def __unicode__(self):
        return self.btitle
    class Meta:
        verbose_name = '品牌'  # 改对象名
        verbose_name_plural = "品牌列表"  # 改表名


