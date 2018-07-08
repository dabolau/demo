from django.apps import AppConfig


class GroupConfig(AppConfig):
    name = 'group'
    ###
    # 定义后台组名称
    # 需要配合__init__.py文件中的配置
    ###
    verbose_name = '班组信息'