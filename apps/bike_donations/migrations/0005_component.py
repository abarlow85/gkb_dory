# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('component_factors', '0002_auto_20160713_0018'),
        ('bike_donations', '0004_auto_20160713_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('handleSelect', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='component_factors.HandlebarOption')),
                ('saddleSelect', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='component_factors.SaddleOption')),
            ],
        ),
    ]
