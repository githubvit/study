# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-16 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ch_adv', '0006_adv1_advstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adv1',
            name='advgoods',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adv_1', to='ch_goods.goodsmangent', verbose_name='\u5546\u54c1'),
        ),
    ]
