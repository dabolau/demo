# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 11:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20171004_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 19, 26, 22, 251311)),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 19, 26, 22, 251311)),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 19, 26, 22, 251311)),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 19, 26, 22, 251311)),
        ),
    ]
