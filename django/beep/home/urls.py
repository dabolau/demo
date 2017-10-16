"""beep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.home, name='home'),  # 首页
    url(r'^login', views.login, name='login'),  # 登录
    url(r'^logout', views.logout, name='logout'),  # 注销

    url(r'^sensor', views.sensor, name='sensor'),  # 传感器页
    url(r'^meter', views.meter, name='meter'),  # 仪表页
    url(r'^option', views.option, name='option'),  # 选项页
    url(r'^mail', views.mail, name='mail'),  # 发送邮件

    url(r'^save', views.save, name='save'),  # 选项数据保存
    url(r'^add', views.add, name='add'),  # 接收传感器数据到数据库
    url(r'^ajax', views.ajax, name='ajax'),  # 传递传感器数据到前端
]
