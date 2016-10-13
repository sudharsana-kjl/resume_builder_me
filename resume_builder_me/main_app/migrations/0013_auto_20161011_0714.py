# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 07:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20161011_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 10, 11, 7, 14, 29, 550453, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 10, 11, 7, 14, 29, 550424, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 10, 11, 7, 14, 29, 549385, tzinfo=utc)),
        ),
    ]