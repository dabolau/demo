"""checkproject URL Configuration

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
    path('', views.account, name='account'),  # 账户首页
    path('main', views.main, name='main'),  # 登录后的页面
    path('login', views.login, name='login'),  # 登录页
    path('logout', views.logout, name='logout'),  # 注销页
    path('register', views.register, name='register'),  # 注册页
    path('changepassword', views.changepassword, name='changepassword'),  # 改密页
    path('reset', views.reset, name='reset'),  # 找回页
]
