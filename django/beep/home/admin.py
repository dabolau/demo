from django.contrib import admin
from home.models import *


###
# 传感器数据库管理模型
###
class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'temperature', 'humidity', 'location',)


###
# 注册数据库模型
###
admin.site.register(Sensor, SensorAdmin)
