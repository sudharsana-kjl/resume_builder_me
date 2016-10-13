# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 06:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20161009_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpa',
            name='sem_no',
            field=models.CharField(choices=[('I', 'Semester I'), ('II', 'Semester II'), ('III', 'Semester III'), ('IV', 'Semester IV'), ('V', 'Semester V'), ('VI', 'Semester VI'), ('VII', 'Semester VII'), ('VIII', 'Semester VIII')], max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 10, 11, 6, 42, 2, 213168, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 10, 11, 6, 42, 2, 213142, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 10, 11, 6, 42, 2, 212097, tzinfo=utc)),
        ),
    ]
