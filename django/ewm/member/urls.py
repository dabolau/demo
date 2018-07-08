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
from member import views

urlpatterns = [
    ###
    # 首页
    ###
    path('', views.member, name='member'),
    ###
    # 详情
    ###
    path('member_detail/', views.member_detail, name='member_detail'),
    ###
    # 添加
    ###
    path('member_add/', views.member_add, name='member_add'),
    ###
    # 编辑
    ###
    path('member_change/', views.member_change, name='member_change'),
    ###
    # 删除
    ###
    path('member_delete/', views.member_delete, name='member_delete'),
]
