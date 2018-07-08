from django.apps import AppConfig


class FileConfig(AppConfig):
    name = 'file'
    ###
    # 定义后台组名称
    # 需要配合__init__.py文件中的配置
    ###
    verbose_name = '附件信息'