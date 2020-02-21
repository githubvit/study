# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def madeorder_handdrawing(request):
    context = {'title': '手绘定制','slogn':'瓷画网传递手工的温度','dzgy':'手绘'}
    return render(request, 'ch_goods/goods-detail-7-1.html', context)
def madeorder_print(request):
    context = {'title': '转印定制', 'slogn': '瓷画网汇集瓷画新工艺', 'dzgy': '转印',
               'minm':'1','maxm':'5000','placeholder':"请在这里输入画面上的文字，20个字符以内免费，最多为100个字符。"}
    return render(request, 'ch_goods/goods-detail-8-2.html', context)
def madeorder_paster(request):
    context = {'title': '贴花定制', 'slogn': '瓷画网汇集瓷画新工艺', 'dzgy': '贴花',
               'minm':'300','maxm':'10000','placeholder':"请在这里输入画面上的文字，最多为100个字符。"}
    return render(request, 'ch_goods/goods-detail-9-1.html', context)