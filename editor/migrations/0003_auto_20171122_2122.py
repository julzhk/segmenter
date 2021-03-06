# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 21:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('editor', '0002_auto_20171122_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='segment',
            name='content_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='BS ITEM'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='segment',
            name='object_id',
            field=models.PositiveIntegerField(default=None),
            preserve_default=False,
        ),
    ]
