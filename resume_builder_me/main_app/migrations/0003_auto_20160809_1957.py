# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20160807_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='resume_file',
        ),
        migrations.AddField(
            model_name='resume',
            name='address',
            field=models.CharField(default='/', max_length=2000),
        ),
    ]
