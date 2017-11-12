from django.contrib import admin
from home.models import *


##############################
# 用户管理数据库模型
##############################
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','fullname', 'mail', 'location', 'level')


##############################
# 选项管理数据库模型
##############################
class OptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')


##############################
# 传感器数据管理数据库模型
##############################
class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'value1', 'value2', 'value3',
                    'value4', 'value5', 'location')


##############################
# 注册用户和用户管理数据库模型
##############################
admin.site.register(User, UserAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Sensor, SensorAdmin)
