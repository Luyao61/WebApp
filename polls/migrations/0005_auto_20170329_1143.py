# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170326_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField(choices=[(60, 60), (80, 80), (100, 100)])),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.EyewitnessStimuli')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userId', models.CharField(max_length=14, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='response',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Users'),
        ),
    ]
