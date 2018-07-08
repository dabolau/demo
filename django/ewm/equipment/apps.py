from django.apps import AppConfig


class EquipmentConfig(AppConfig):
    name = 'equipment'
    ###
    # 定义后台组名称
    # 需要配合__init__.py文件中的配置
    ###
    verbose_name = '设备信息'
