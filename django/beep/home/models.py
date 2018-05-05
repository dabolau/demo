from django.db import models


###
# 传感器数据库模型
###
class Sensor(models.Model):
    name = models.CharField(verbose_name='名称',
                            max_length=64,)
    temperature = models.SmallIntegerField(verbose_name='温度',)
    humidity = models.SmallIntegerField(verbose_name='湿度',)
    location = models.CharField(verbose_name='位置',
                                max_length=64)
    create_time = models.DateTimeField(
        verbose_name='创建时间', auto_now_add=True,)
    update_time = models.DateTimeField(
        verbose_name='更新时间', auto_now=True,)

    class Meta:
        verbose_name = '传感器'
        verbose_name_plural = '传感器'

    def __str__(self):
        return self.name
