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
from file import views

urlpatterns = [
    ###
    # 首页
    ###
    path('', views.file, name='file'),
    ###
    # 详情
    ###
    path('file_detail/', views.file_detail, name='file_detail'),
    ###
    # 添加
    ###
    path('file_add/', views.file_add, name='file_add'),
    ###
    # 编辑
    ###
    path('file_change/', views.file_change, name='file_change'),
    ###
    # 删除
    ###
    path('file_delete/', views.file_delete, name='file_delete'),
]
