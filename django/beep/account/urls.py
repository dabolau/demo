from django.urls import path
from account import views

urlpatterns = [
    # 账户首页
    path('', views.account, name='account'),
    # 账户登录
    path('login', views.login, name='login'),
    # 账户注销
    path('logout', views.logout, name='logout'),
]
