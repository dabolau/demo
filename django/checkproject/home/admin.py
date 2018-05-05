from django.contrib import admin
from home.models import *

# 注册数据库模型（步骤）
admin.site.register(Bjs_base_step)

# 注册数据库模型（双电源切换柜）
admin.site.register(Bjs_base_dual_power_switching)
# 注册数据库模型（蓄电池电源主机柜）
admin.site.register(Bjs_base_battery_power_mainframe)
# 注册数据库模型（分时下电柜）
admin.site.register(Bjs_base_power_off_mainframe)
# 注册数据库模型（电池柜）
admin.site.register(Bjs_base_battery_mainframe)
# 注册数据库模型（巡检记事）
admin.site.register(Bjs_base_other_situation)
