# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20170329_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='answer',
            field=models.IntegerField(choices=[(60, 60), (80, 80), (100, 100)], null=True),
        ),
    ]
