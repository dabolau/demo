from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'home'
    ###
    # 定义后台组名称
    # 需要配合__init__.py文件中的配置
    ###
    verbose_name = '网站信息'