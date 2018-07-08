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
from account import views

urlpatterns = [
    ###
    # 首页
    ###
    path('', views.account, name='account'),
    ###
    # 登录
    ###
    path('login/', views.login, name='login'),
    ###
    # 注册
    ###
    path('register/', views.register, name='register'),
    ###
    # 修改密码
    ###
    path('changepassword/', views.changepassword, name='changepassword'),
    ###
    # 找回密码
    ###
    path('getpassword/', views.getpassword, name='getpassword'),
    ###
    # 注销
    ###
    path('logout/', views.logout, name='logout'),
]
