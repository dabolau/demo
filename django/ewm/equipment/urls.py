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
from equipment import views

urlpatterns = [
    ###
    # 首页
    ###
    path('', views.equipment, name='equipment'),
    ###
    # 详情
    ###
    path('equipment_detail/', views.equipment_detail, name='equipment_detail'),
    ###
    # 添加
    ###
    path('equipment_add/', views.equipment_add, name='equipment_add'),
    ###
    # 编辑
    ###
    path('equipment_change/', views.equipment_change, name='equipment_change'),
    ###
    # 删除
    ###
    path('equipment_delete/', views.equipment_delete, name='equipment_delete'),
]
