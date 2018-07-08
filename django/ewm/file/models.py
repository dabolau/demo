from django.db import models


###
# 附件信息数据库模型
###
class File(models.Model):
    '''
    附件信息数据库模型
    '''
    file_name = models.CharField(
        verbose_name='文件名称',
        max_length=32,
        unique=True,  #唯一标示
    )
    tag_list = (
        ('班组照片', '班组照片'),
        ('员工照片', '员工照片'),
        ('设备照片', '设备照片'),
        # ('党建工作', '党建工作'),
        # ('应知应会', '应知应会'),
        # ('岗位责任', '岗位责任'),
        # ('风险源识别', '风险源识别'),
        # ('安全隐患', '安全隐患'),
        # ('安全规程', '安全规程'),
        # ('应急预案', '应急预案'),
        ('其它附件', '其它附件'),
    )
    file_tag = models.CharField(
        verbose_name='文件标签',
        max_length=32,
        choices=tag_list,
    )
    file_upload = models.FileField(
        verbose_name='文件信息',
        upload_to='static/file/%Y%m%d/',
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
        verbose_name = '附件信息'
        verbose_name_plural = '附件信息'

    def __str__(self):
        return self.file_name