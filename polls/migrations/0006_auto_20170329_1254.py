# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 16:54
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20170329_1143'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='eyewitnessstimuli',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
