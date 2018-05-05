from django.urls import path
from home import views

urlpatterns = [
    # 控制台首页
    path('', views.home, name='home'),
    # 界面视图
    path('sensor', views.sensor, name='sensor'),  # 传感器页
    path('meter', views.meter, name='meter'),  # 仪表页
    # 传感器和数据库交互信息
    path('add', views.add, name='add'),  # 接收传感器数据到数据库
    path('ajax', views.ajax, name='ajax'),  # 传递传感器数据到前端
    # # 警告信息发送
    path('mail', views.mail, name='mail'),  # 发送邮件
]
