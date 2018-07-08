from django.contrib import admin
from home.models import *

###
# 后台登录设置
###
admin.site.site_header = '智能云端'
admin.site.site_title = '智能云端'


###
# 注册网站信息数据库模型和自定义功能
###
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    ###
    # 管理中要显示的字段名称
    ###
    list_display = [
        'web_name',
        'web_content',
        'web_status',
    ]
    ###
    # 管理中要搜索的字段名称
    ###
    search_fields = [
        'web_name',
        'web_content',
        'web_status',
    ]
