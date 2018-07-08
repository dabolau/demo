from django.contrib import admin
from equipment.models import *


###
# 注册设备履历数据库模型和自定义功能
###
@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    ###
    # 管理中要显示的字段名称
    ###
    list_display = [
        'equipment_name',
        'manufacturer_name',
        'model_specification',
        'equipment_location',
        'enable_date',
    ]
    ###
    # 管理中要搜索的字段名称
    ###
    search_fields = [
        'equipment_name',
        'manufacturer_name',
        'model_specification',
        'equipment_location',
        'enable_date',
    ]
    ###
    # 管理中有筛选框的字段名称
    ###
    filter_horizontal = [
        'other_information',
    ]
