# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 11:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20171004_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '选项',
                'verbose_name_plural': '选项',
            },
        ),
        migrations.AlterField(
            model_name='sensor',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 19, 32, 14, 988542)),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 19, 32, 14, 988542)),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 19, 32, 14, 988542)),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 19, 32, 14, 988542)),
        ),
    ]
