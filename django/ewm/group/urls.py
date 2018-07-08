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

from django.urls import path
from group import views

urlpatterns = [
    ###
    # 首页
    ###
    path('', views.group, name='group'),
    ###
    # 详情
    ###
    path('group_detail/', views.group_detail, name='group_detail'),
    ###
    # 添加
    ###
    path('group_add/', views.group_add, name='group_add'),
    ###
    # 编辑
    ###
    path('group_change/', views.group_change, name='group_change'),
    ###
    # 删除
    ###
    path('group_delete/', views.group_delete, name='group_delete'),
]
