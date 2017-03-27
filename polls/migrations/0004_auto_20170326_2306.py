# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_eyewitnessstimuli'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eyewitnessstimuli',
            name='lineup_number',
            field=models.CharField(choices=[('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B4'), ('B5', 'B5'), ('B6', 'B6'), ('W1', 'W1'), ('W2', 'W2'), ('W3', 'W3'), ('W4', 'W4'), ('W5', 'W5'), ('W6', 'W6')], max_length=2),
        ),
    ]
