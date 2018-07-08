from django.contrib import admin
from file.models import *


###
# 注册附件信息数据库模型和自定义功能
###
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    ###
    # 管理中要显示的字段名称
    ###
    list_display = [
        'file_name',
        # 'manufacturer_name',
        # 'model_specification',
        # 'equipment_location',
        # 'enable_date',
    ]
    ###
    # 管理中要搜索的字段名称
    ###
    search_fields = [
        'file_name',
        # 'manufacturer_name',
        # 'model_specification',
        # 'equipment_location',
        # 'enable_date',
    ]
