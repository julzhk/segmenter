# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 21:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0003_auto_20171122_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balancesheetitem',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='balancesheetitem',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='segment',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='segment',
            name='object_id',
        ),
    ]
