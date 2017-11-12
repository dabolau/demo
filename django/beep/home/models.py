from django.db import models
from datetime import *


##############################
# 用户数据库模型
##############################
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    location = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    create_time = models.DateTimeField(default=datetime.now())
    update_time = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.username


##############################
# 选项数据库模型
##############################
class Option(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    class Meta:
        verbose_name = '选项'
        verbose_name_plural = '选项'

    def __str__(self):
        return self.name


##############################
# 传感器数据库模型
##############################
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    value1 = models.CharField(max_length=50)
    value2 = models.CharField(max_length=50)
    value3 = models.CharField(max_length=50)
    value4 = models.CharField(max_length=50)
    value5 = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    create_time = models.DateTimeField(default=datetime.now())
    update_time = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = '传感器数据'
        verbose_name_plural = '传感器数据'

    def __str__(self):
        return self.name
