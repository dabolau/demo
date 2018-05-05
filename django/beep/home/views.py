from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from home.models import *
from datetime import *

import time


###
# 首页
###
# @login_required(login_url='/account/login')
def home(request):
    return HttpResponseRedirect('/sensor')


###
# 404页面，开启需要将配置修改为（DEBUG=False）
###
def page_not_found(request):
    return render(request, '404.html', locals())


###
# 500页面，开启需要将配置修改为（DEBUG=False）
###
def page_error(request):
    return render(request, '500.html', locals())


###
# 传感器
###
@login_required(login_url='/account/login')
def sensor(request):
    # 设置温度报警值
    temperature_value = 35
    # 设置湿度报警值
    humidity_value = 10
    if request.method == 'GET':
        text = request.GET.get('text')
        if text == None:
            return HttpResponseRedirect('/sensor?text=')
        else:
            # 查询传感器数据库中的数据
            sensor_all = Sensor.objects.filter(
                location__contains=text).order_by('-id')
            # 传感器数据分页
            paginator = Paginator(sensor_all, 10)  # 每页显示一条数据
            page = request.GET.get('page')
            try:
                sensor = paginator.page(page)
            except PageNotAnInteger:
                sensor = paginator.page(1)  # 如果页面不是整数跳到第一页
            except EmptyPage:
                sensor = paginator.page(
                    paginator.num_pages)  # 如果页面超出最大范围跳到最后一页

            # 输出图表中总计，车间、白居寺、白居寺车场、大堰、大堰车场、大坪
            all_location_count = Sensor.objects.filter(
                location__contains=text).count()
            baijusi_location_count = Sensor.objects.filter(
                location__contains=text,
                location='白居寺站',
                temperature__lt=temperature_value).count()
            baijusichechang_location_count = Sensor.objects.filter(
                location__contains=text,
                location='白居寺车场',
                temperature__lt=temperature_value).count()
            dayan_location_count = Sensor.objects.filter(
                location__contains=text,
                location='大堰站',
                temperature__lt=temperature_value).count()
            dayanchechang_location_count = Sensor.objects.filter(
                location__contains=text,
                location='大堰车场',
                temperature__lt=temperature_value).count()
            daping_location_count = Sensor.objects.filter(
                location__contains=text,
                location='大坪站',
                temperature__lt=temperature_value).count()

            # 输出图表中总计，车间、白居寺、白居寺车场、大堰、大堰车场、大坪
            all2_location_count = Sensor.objects.filter(
                location__contains=text).count()
            baijusi2_location_count = Sensor.objects.filter(
                location__contains=text,
                location='白居寺站',
                temperature__gte=temperature_value).count()
            baijusichechang2_location_count = Sensor.objects.filter(
                location__contains=text,
                location='白居寺车场',
                temperature__gte=temperature_value).count()
            dayan2_location_count = Sensor.objects.filter(
                location__contains=text,
                location='大堰站',
                temperature__gte=temperature_value).count()
            dayanchechang2_location_count = Sensor.objects.filter(
                location__contains=text,
                location='大堰车场',
                temperature__gte=temperature_value).count()
            daping2_location_count = Sensor.objects.filter(
                location__contains=text,
                location='大坪站',
                temperature__gte=temperature_value).count()

            # 显示页面
            return render(request, 'sensor.html', locals())


###
# 仪表页
###
@login_required(login_url='/account/login')
def meter(request):
    # 判断是否为（GET）方式提交
    if request.method == 'GET':
        # 获取提交表单中的设备名称
        name = request.GET['name']
    # 显示页面
    return render(request, 'meter.html', locals())


###
# 数据提交到数据库（add?name=设备名称&location=设备位置&temperature=温度值&humidity=湿度值）
###
def add(request):
    # 判断是否为（GET）方式提交
    if request.method == 'GET':
        # 获取表单中的数据
        name = request.GET['name']
        location = request.GET['location']
        temperature = request.GET['temperature']  # 表示温度
        humidity = request.GET['humidity']  # 表示湿度
        # 添加到数据库
        Sensor.objects.create(
            name=name,
            location=location,
            temperature=temperature,
            humidity=humidity,
        )

        ###
        # 判断是否发送警告邮件
        ###
        # 设置温度报警值
        temperature_value = 35
        # 设置湿度报警值
        humidity_value = 10
        if int(temperature) >= temperature_value:
            # 发送邮件
            return HttpResponseRedirect(
                '/mail?name=' + name + '&location=' + location +
                '&temperature=' + temperature + '&humidity=' + humidity)

        # 格式化为（JSON）数据形式
        data = {
            'name': name,
            'location': location,
            'temperature': temperature,
            'humidity': humidity,
        }
    # 返回（JSON）数据到页面
    return JsonResponse(data)


###
# 数据提交到前端（ajax?name=设备名称）
###
def ajax(request):
    # 判断是否为（GET）方式提交
    if request.method == 'GET':
        # 获取提交表单中的设备名称
        name = request.GET['name']
        # 获取传感器数据库中某设备名称的数据并按（ID）编号倒序排列
        data_all_count = Sensor.objects.filter(
            name__exact=name).order_by('-id')
        # 获取传感器数据库中某设备名称的最后一条数据
        data = Sensor.objects.get(id__exact=data_all_count[0].id)
        # 格式化为（JSON）数据形式
        data = {
            'id': data.id,
            'name': data.name,
            'location': data.location,
            'temperature': data.temperature,
            'humidity': data.humidity,
            'create_time': data.create_time,
            'update_time': data.update_time,
        }
        # 返回（JSON）数据到页面
        return JsonResponse(data)


###
# 发送邮件（mail?name=设备名称&location=设备位置&temperature=温度值&humidity=湿度值）
###
def mail(request):
    # 获取传感器数据库中数据的总数（相当于最后一条数据）
    data_all_count = Sensor.objects.all().count()
    # 查询传感器数据库中最后一条数据
    data = Sensor.objects.get(id__exact=data_all_count)
    # 获取表单中的数据
    name = request.GET['name']
    location = request.GET['location']
    temperature = request.GET['temperature']  # 表示温度
    humidity = request.GET['humidity']  # 表示湿度
    # 获取用户数据库中的所有数据
    user = User.objects.filter(groups__name=location)
    print(user)
    for u in user:
        # 发送邮件
        send_mail(
            '警告信息',
            '警告信息，时间（' + str(data.create_time) + '），名称（' + data.name +
            '），位置（' + data.location + '），温度（' + str(data.temperature) +
            '），湿度（' + str(data.humidity) + '），请立即检查。',
            '警告信息<dabolau@163.com>',
            [u.email],
        )
        print(u.email)

    # 格式化为（JSON）数据形式
    data = {
        'id': data.id,
        'name': data.name,
        'location': data.location,
        'temperature': data.temperature,
        'humidity': data.humidity,
        'create_time': data.create_time,
        'update_time': data.update_time,
    }
    # 返回（JSON）数据到页面
    return JsonResponse(data)
