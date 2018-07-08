from django.db import models
from file.models import *


###
# 员工信息数据库模型
###
class Member(models.Model):
    '''
    员工信息数据库模型
    '''
    member_photo = models.ManyToManyField(
        to=File,
        verbose_name='员工照片',
        limit_choices_to={'file_tag': '员工照片'},
    )
    member_number = models.IntegerField(verbose_name='工号', )
    member_name = models.CharField(
        verbose_name='姓名',
        max_length=32,
        unique=True,  #唯一标示
    )
    sex_list = (
        ('男', '男'),
        ('女', '女'),
    )
    member_sex = models.CharField(
        verbose_name='性别',
        max_length=32,
        choices=sex_list,
    )
    member_birthday = models.CharField(
        verbose_name='出生日期',
        max_length=32,
    )
    entry_time = models.CharField(
        verbose_name='入司时间',
        max_length=32,
    )
    member_company = models.CharField(
        verbose_name='公司',
        max_length=32,
        default='重庆市轨道交通（集团）有限公司',
    )
    member_department = models.CharField(
        verbose_name='部门',
        max_length=32,
    )
    member_position = models.CharField(
        verbose_name='岗位/职务',
        max_length=32,
    )
    level_list = (
        ('初一', '初一'),
        ('初二', '初二'),
        ('初三', '初三'),
        ('中一', '中一'),
        ('中二', '中二'),
        ('中三', '中三'),
        ('高一', '高一'),
        ('高二', '高二'),
        ('高三', '高三'),
        ('技师', '技师'),
        ('高级技师', '高级技师'),
    )
    member_level = models.CharField(
        verbose_name='技能等级',
        max_length=32,
        choices=level_list,
    )
    political_list = (
        ('中共党员', '中共党员'),
        ('中共预备党员', '中共预备党员'),
        ('入党积极分子', '入党积极分子'),
        ('共青团员', '共青团员'),
        # ('民革党员', '民革党员'),
        # ('民盟盟员', '民盟盟员'),
        # ('民建会员', '民建会员'),
        # ('民进会员', '民进会员'),
        # ('农工党党员', '农工党党员'),
        # ('致公党党员', '致公党党员'),
        ('九三学社社员', '九三学社社员'),
        # ('台盟盟员', '台盟盟员'),
        ('无党派人士', '无党派人士'),
        ('群众', '群众'),
    )
    political_status = models.CharField(
        verbose_name='政治面貌',
        max_length=32,
        choices=political_list,
    )
    member_phone = models.BigIntegerField(verbose_name='联系电话', )
    member_email = models.EmailField(
        verbose_name='邮箱',
        max_length=32,
    )
    member_introduction = models.TextField(verbose_name='员工简介', )
    member_other = models.TextField(verbose_name='其它信息', )
    create_time = models.DateTimeField(
        verbose_name='创建时间',
        auto_now_add=True,
    )
    update_time = models.DateTimeField(
        verbose_name='创建时间',
        auto_now=True,
    )

    class Meta:
        verbose_name = '员工信息'
        verbose_name_plural = '员工信息'

    def __str__(self):
        return self.member_name