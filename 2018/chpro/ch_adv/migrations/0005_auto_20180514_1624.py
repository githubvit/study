# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-14 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ch_adv', '0004_auto_20180514_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='adv1',
            name='advpic1art',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='\u9996\u9875\u8df3\u8f6c\u56fe\u7247\u63d0\u793a'),
        ),
        migrations.AddField(
            model_name='adv1',
            name='advpic2art',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='\u6b21\u9875\u56fe\u7247\u63d0\u793a'),
        ),
        migrations.AlterField(
            model_name='adv1',
            name='advgoods',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adv_1', to='ch_goods.goodsinfo', verbose_name='\u5546\u54c1'),
        ),
        migrations.AlterField(
            model_name='adv1',
            name='advgt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adv_1', to='ch_goods.goodstype', verbose_name='\u7c7b\u522b'),
        ),
        migrations.AlterField(
            model_name='adv1',
            name='advtp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adv_1', to='ch_adv.adv1type', verbose_name='\u9996\u9875\u4f4d\u7f6e'),
        ),
        migrations.AlterField(
            model_name='adv1',
            name='advuser',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='adv_1', to='ch_supplier.SupplierInfo', verbose_name='\u5185\u5bb9\u53d1\u5e03\u4eba'),
        ),
    ]