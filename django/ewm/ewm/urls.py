"""ewm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    ###
    # 管理应用
    ###
    path('admin/', admin.site.urls),
    ###
    # 首页应用
    ###
    path('', include('home.urls')),
    ###
    # 账户应用，功能注册、登录、修改密码、找回密码、注销
    ###
    path('account/', include('account.urls')),
    ###
    # 用户应用，功能添加用户、编辑用户、删除用户
    ###
    path('user/', include('user.urls')),
    ###
    # 班组应用
    ###
    path('group/', include('group.urls')),
    ###
    # 员工应用
    ###
    path('member/', include('member.urls')),
    ###
    # 设备应用
    ###
    path('equipment/', include('equipment.urls')),
    ###
    # 附件应用
    ###
    path('file/', include('file.urls')),
]
