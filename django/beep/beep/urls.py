from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # 首页
    path('account/', include('account.urls')),  # 用户
]
