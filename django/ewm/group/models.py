from django.db import models
from member.models import *
from equipment.models import *
from file.models import *


###
# 班组信息数据库模型
###
class Group(models.Model):
    '''
    班组信息数据库模型
    '''
    group_photo = models.ManyToManyField(
        to=File,
        verbose_name='班组照片',
        limit_choices_to={'file_tag': '班组照片'},
        related_name='班组照片',
    )
    group_name = models.CharField(
        verbose_name='班组名称',
        max_length=32,
        unique=True,
    )
    group_location = models.CharField(
        verbose_name='班组地址',
        max_length=32,
    )
    group_phone = models.BigIntegerField(verbose_name='班组电话', )
    group_introduction = models.TextField(verbose_name='班组简介', )
    group_member = models.ManyToManyField(
        to=Member,
        verbose_name='班组成员',
    )
    group_equipment = models.ManyToManyField(
        to=Equipment,
        verbose_name='班组设备',
    )
    group_other_information = models.ManyToManyField(
        to=File,
        verbose_name='其它附件',
        limit_choices_to={'file_tag': '其它附件'},
        related_name='班组信息其它附件',  # 这个属性在整个系统中不能重复
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
        verbose_name = '班组信息'
        verbose_name_plural = '班组信息'

    def __str__(self):
        return self.group_name