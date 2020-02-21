# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 评价
# class evaluation(models.Model):
#     econtext=models.CharField(max_length=64,verbose_name="评价内容")
#     epic=models.ImageField(upload_to='ch_goods',verbose_name='评价贴图')
#     euser=models.ForeignKey(models.UserInfo,related_name="e_user",verbose_name="评价用户")
#     egoods=models.ForeignKey(goodsinfo,related_name="e_goods",verbose_name="评价商品")