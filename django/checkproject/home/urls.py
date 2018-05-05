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
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path(
        'add_bjs_base_step_start',
        views.add_bjs_base_step_start,
        name='add_bjs_base_step_start'),
    path(
        'add_bjs_base_step_end',
        views.add_bjs_base_step_end,
        name='add_bjs_base_step_end'),
    #############
    # 双电源切换柜
    #############
    path(
        'list_bjs_base_dual_power_switching',
        views.list_bjs_base_dual_power_switching,
        name='list_bjs_base_dual_power_switching'),
    path(
        'page_bjs_base_dual_power_switching',
        views.page_bjs_base_dual_power_switching,
        name='page_bjs_base_dual_power_switching'),
    path(
        'add_bjs_base_dual_power_switching',
        views.add_bjs_base_dual_power_switching,
        name='add_bjs_base_dual_power_switching'),
    path(
        'change_bjs_base_dual_power_switching',
        views.change_bjs_base_dual_power_switching,
        name='change_bjs_base_dual_power_switching'),
    path(
        'delete_bjs_base_dual_power_switching',
        views.delete_bjs_base_dual_power_switching,
        name='delete_bjs_base_dual_power_switching'),
    #################
    # 蓄电池电源主机柜
    #################
    path(
        'add_bjs_base_battery_power_mainframe',
        views.add_bjs_base_battery_power_mainframe,
        name='add_bjs_base_battery_power_mainframe'),
    path(
        'change_bjs_base_battery_power_mainframe',
        views.change_bjs_base_battery_power_mainframe,
        name='change_bjs_base_battery_power_mainframe'),
    path(
        'delete_bjs_base_battery_power_mainframe',
        views.delete_bjs_base_battery_power_mainframe,
        name='delete_bjs_base_battery_power_mainframe'),

    #################
    # 分时下电柜
    #################
    path(
        'add_bjs_base_power_off_mainframe',
        views.add_bjs_base_power_off_mainframe,
        name='add_bjs_base_power_off_mainframe'),
    path(
        'change_bjs_base_power_off_mainframe',
        views.change_bjs_base_power_off_mainframe,
        name='change_bjs_base_power_off_mainframe'),
    path(
        'delete_bjs_base_power_off_mainframe',
        views.delete_bjs_base_power_off_mainframe,
        name='delete_bjs_base_power_off_mainframe'),

    #################
    # 电池柜
    #################
    path(
        'add_bjs_base_battery_mainframe',
        views.add_bjs_base_battery_mainframe,
        name='add_bjs_base_battery_mainframe'),
    path(
        'change_bjs_base_battery_mainframe',
        views.change_bjs_base_battery_mainframe,
        name='change_bjs_base_battery_mainframe'),
    path(
        'delete_bjs_base_battery_mainframe',
        views.delete_bjs_base_battery_mainframe,
        name='delete_bjs_base_battery_mainframe'),

    #################
    # 巡检记事
    #################
    path(
        'add_bjs_base_other_situation',
        views.add_bjs_base_other_situation,
        name='add_bjs_base_other_situation'),
    path(
        'change_bjs_base_other_situation',
        views.change_bjs_base_other_situation,
        name='change_bjs_base_other_situation'),
    path(
        'delete_bjs_base_other_situation',
        views.delete_bjs_base_other_situation,
        name='delete_bjs_base_other_situation'),
]
