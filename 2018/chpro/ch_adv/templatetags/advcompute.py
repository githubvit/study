# -*- coding: utf-8 -*-
'''
计算
'''
from django import template
from django.utils.safestring import mark_safe

register=template.Library()

# 计算单价（商品对象，单价率）
@register.simple_tag
def pricerst(goods, gxprice):
    price1 = float()
    for i in goods:
        price1 += float(i.sprice * i.num)
        print price1
    price2 = price1 * float(gxprice)

    return price2