from django.contrib import admin
from member.models import *


###
# 注册员工信息数据库模型和自定义功能
###
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    ###
    # 管理中要显示的字段名称
    ###
    list_display = [
        'member_name',
        'member_number',
        'member_sex',
        # 'member_birthday',
        'member_company',
        'member_department',
        'member_position',
        'member_phone',
        # 'member_email',
        # 'member_introduction',
        # 'member_other',
    ]
    ###
    # 管理中要搜索的字段名称
    ###
    search_fields = [
        'member_name',
        'member_number',
        'member_sex',
        'member_birthday',
        'member_company',
        'member_department',
        'member_position',
        'member_phone',
        'member_email',
        'member_introduction',
        'member_other',
    ]
