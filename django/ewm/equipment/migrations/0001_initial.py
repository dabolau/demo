# Generated by Django 2.0 on 2018-09-17 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(max_length=32, unique=True, verbose_name='设备名称')),
                ('manufacturer_name', models.CharField(max_length=32, verbose_name='制造商名称')),
                ('model_specification', models.CharField(max_length=32, verbose_name='型号/规格')),
                ('equipment_location', models.CharField(max_length=32, verbose_name='存放位置')),
                ('enable_date', models.CharField(max_length=32, verbose_name='启用日期')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('equipment_photo', models.ManyToManyField(limit_choices_to={'file_tag': '设备照片'}, related_name='设备照片', to='file.File', verbose_name='设备照片')),
                ('other_information', models.ManyToManyField(limit_choices_to={'file_tag': '其它附件'}, related_name='设备信息其它附件', to='file.File', verbose_name='其它附件')),
            ],
            options={
                'verbose_name': '设备信息',
                'verbose_name_plural': '设备信息',
            },
        ),
    ]
