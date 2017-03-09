# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 09:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170308_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='i_by',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='i_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 3, 9, 9, 11, 12, 89109, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='u_by',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='u_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]