from django.contrib import admin
from group.models import *


###
# 注册班组信息数据库模型和自定义功能
###
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    ###
    # 管理中要显示的字段名称
    ###
    list_display = [
        'group_name',
        'group_location',
        'group_phone',
        # 'group_introduction',
        # 'group_member',
        # 'group_equipment',
        # 'group_other_information',
    ]
    ###
    # 管理中要搜索的字段名称
    ###
    search_fields = [
        'group_name',
        'group_location',
        'group_phone',
        'group_introduction',
        'group_member',
        'group_equipment',
        'group_other_information',
    ]
    ###
    # 管理中有筛选框的字段名称
    ###
    filter_horizontal = [
        'group_member',
        'group_equipment',
        'group_other_information',
    ]
