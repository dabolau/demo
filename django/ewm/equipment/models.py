from django.db import models
from file.models import *


###
# 设备履历数据库模型
###
class Equipment(models.Model):
    '''
    设备履历数据库模型
    '''
    equipment_photo = models.ManyToManyField(
        to=File,
        verbose_name='设备照片',
        limit_choices_to={'file_tag': '设备照片'},
        related_name='设备照片',
    )
    equipment_name = models.CharField(
        verbose_name='设备名称',
        max_length=32,
        unique=True,  #唯一标示
    )
    manufacturer_name = models.CharField(
        verbose_name='制造商名称',
        max_length=32,
    )
    model_specification = models.CharField(
        verbose_name='型号/规格',
        max_length=32,
    )
    equipment_location = models.CharField(
        verbose_name='存放位置',
        max_length=32,
    )
    enable_date = models.CharField(
        verbose_name='启用日期',
        max_length=32,
    )
    # html_file = models.FileField(
    #     verbose_name='技术资料',
    #     upload_to='static/html/',
    # )
    # other_file = models.FileField(
    #     verbose_name='其他资料',
    #     upload_to='static/other/',
    # )
    other_information = models.ManyToManyField(
        to=File,
        verbose_name='其它附件',
        limit_choices_to={'file_tag': '其它附件'},
        related_name='设备信息其它附件',  # 这个属性在整个系统中不能重复
    )
    create_time = models.DateTimeField(
        verbose_name='创建时间',
        auto_now_add=True,
    )
    update_time = models.DateTimeField(
        verbose_name='创建时间',
        auto_now=True,
    )

    class Meta:
        verbose_name = '设备信息'
        verbose_name_plural = '设备信息'

    def __str__(self):
        return self.equipment_name