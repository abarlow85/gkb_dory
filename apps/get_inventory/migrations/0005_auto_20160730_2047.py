# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-30 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_inventory', '0004_auto_20160729_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customsku',
            name='customSku',
            field=models.CharField(max_length=13),
        ),
    ]
