# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0011_segment_logic_segment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('segments', models.ManyToManyField(blank=True, null=True, to='editor.Segment')),
            ],
        ),
    ]
