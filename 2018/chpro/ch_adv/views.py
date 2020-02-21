# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
from advcontrol import advcrl
# Create your views here.
# 价格计算
def pricerst(goods, gxprice):
    price1 = float()#建立float空变量
    for i in goods:
        price1 += float(i.sprice * i.num)
        #这里挺好玩，这边必须加float将规格的计算结果转为float，但在自定义模板函数simple_tag中可以不用
        print price1
    price2 = price1 * float(gxprice)

    return price2

# 首页显示
def index(request):
    adv1_dic=advcrl(adv1)
    adv1_li1=adv1_dic[1]
    adv1_li2=adv1_dic[2]
    adv1_li3=adv1_dic[3]
    adv1_li4=adv1_dic[4]
    print adv1_dic
    print adv1_li1
    print adv1_li2
    for i in adv1_li2:
        print i.advgoods.gmgoods.s_goods.all()
        print '价格='+str(pricerst(i.advgoods.gmgoods.s_goods.all(),i.advgoods.gxprice))
    print adv1_li3
    print adv1_li4
    context={'title':'首页',
             'adv1_li1':adv1_li1,'li1_count':range(adv1_li1.__len__()),
             'adv1_li2':adv1_li2,'li2_count':range(adv1_li2.__len__()),
             'adv1_li3':adv1_li3,'li3_count':range(adv1_li3.__len__()),
             'adv1_li4':adv1_li4,'li4_count':range(adv1_li4.__len__()),
             }
    return render(request, 'adv/adv1/index-1.html', context)
