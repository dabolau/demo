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
from user import views

urlpatterns = [
    ###
    # 首页
    ###
    path('', views.user, name='user'),
    ###
    # 添加
    ###
    path('user_add/', views.user_add, name='user_add'),
    ###
    # 编辑
    ###
    path('user_change/', views.user_change, name='user_change'),
    ###
    # 删除
    ###
    path('user_delete/', views.user_delete, name='user_delete'),
]
