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
from home import views

urlpatterns = [
    ###
    # 首页地址
    ###
    path('', views.home, name='home'),
    ###
    # 首页地址
    ###
    path('main/', views.main, name='main'),
    ###
    # 关于及错误报告地址
    ###
    path('bug/', views.bug, name='bug'),
    ###
    # 网站信息地址
    ###
    path('note/', views.note, name='note'),
]
