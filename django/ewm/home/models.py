from django.db import models


###
# 网站信息数据库模型
###
class Home(models.Model):
    '''
    网站信息数据库模型
    '''
    status_list = (
        ('打开', '打开'),
        ('关闭', '关闭'),
    )
    web_name = models.CharField(
        verbose_name='名称',
        max_length=32,
        unique=True,
    )
    web_content = models.TextField(
        verbose_name='内容描述',
        max_length=255,
    )
    web_status = models.CharField(
        verbose_name='开关',
        max_length=32,
        choices=status_list,
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
        verbose_name = '网站信息'
        verbose_name_plural = '网站信息'

    def __str__(self):
        return self.web_name