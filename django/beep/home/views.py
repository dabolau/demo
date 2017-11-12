##############################
# 版权归作者所有
# 作者：刘毅
# 日期：20170930
# 版本号：1.0
##############################
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.core.mail import send_mail
from home.models import *

from datetime import *

import itchat
import time


##############################
# 首页
##############################
def home(request):
    # 获取服务器（SESSION）用户信息
    username = request.session.get('username', None)
    if username:
        # 服务器（SESSION）用户信息不为空，跳转到产品页面
        response = HttpResponseRedirect('/sensor')
        return response
    else:
        # 服务器（SESSION）用户信息为空，跳转到登录页面
        response = HttpResponseRedirect('/login')
        return response


##############################
# 登录
##############################
def login(request):
    # 判断是否为安全（POST）方式提交
    if request.method == 'POST':
        # 获取提交表单中的用户和密码
        username = request.POST['username']
        password = request.POST['password']
        # 判断表单中的用户和密码是否与数据库中的用户和密码完全相同
        user = User.objects.filter(
            username__exact=username, password__exact=password)
        if user:
            # 如果用户和密码相同，将用户名存入服务器（SESSION）
            request.session['username'] = username
            # 服务器（SESSION）失效时间设置以秒为单位，其中（0）表示关闭浏览器失效
            request.session.set_expiry(0)
            # 如果用户和密码相同，跳转到管理页面
            response = HttpResponseRedirect('/sensor')
            return response
        else:
            # 如果用户和密码不相同，返回登录失败的信息
            message = '登录失败，用户或密码错误。'
    else:
        pass
    # 显示登录页
    return render(request, 'login.html', locals())


##############################
# 注销
##############################
def logout(request):
    try:
        # 删除服务器（SESSION）
        del request.session['username']
    except KeyError:
        pass
    # 跳转到登录页
    response = HttpResponseRedirect('/login')
    return response


##############################
# 404页面，开启需要将配置修改为（DEBUG=False）
##############################
def page_not_found(request):
    return render(request, '404.html', locals())


##############################
# 500页面，开启需要将配置修改为（DEBUG=False）
##############################
def page_error(request):
    return render(request, '500.html', locals())


##############################
# 传感器页
##############################
def sensor(request):
    # 获取服务器（SESSION）用户信息
    username = request.session.get('username', None)
    if username:
        if request.method == 'GET':
            text = request.GET.get('text')
            if text == None:
                response = HttpResponseRedirect('/sensor?text=')
                return response

            else:
                # 获取选项数据库中的数据
                temperature = Option.objects.get(name='temperature')
                humidity = Option.objects.get(name='humidity')

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
                chejian_location_count = Sensor.objects.filter(
                    location__contains=text,
                    location='车间',
                    value1__lt=temperature.value).count()
                baijusi_location_count = Sensor.objects.filter(
                    location__contains=text,
                    location='白居寺',
                    value1__lt=temperature.value).count()
                baijusichechang_location_count = Sensor.objects.filter(
                    location__contains=text,
                    location='白居寺车场',
                    value1__lt=temperature.value).count()
                dayan_location_count = Sensor.objects.filter(
                    location__contains=text,
                    location='大堰',
                    value1__lt=temperature.value).count()
                dayanchechang_location_count = Sensor.objects.filter(
                    location__contains=text,
                    location='大堰车场',
                    value1__lt=temperature.value).count()
                daping_location_count = Sensor.objects.filter(
                    location__contains=text,
                    location='大坪',
                    value1__lt=temperature.value).count()

                # 输出图表中总计，车间、白居寺、白居寺车场、大堰、大堰车场、大坪
                all2_location_count = Sensor.objects.filter(
                    location__contains=text).count()
                chejian2_location_count = Sensor.objects.filter(
                    location__contains=text,
                    location='车间',
                    value1__gte=temperature.value).count()
                baijusi2_location_count = Sensor.objects.filter(
                    location__contains=text,
                    location='白居寺',
                    value1__gte=temperature.value).count()
                baijusichechang2_location_count = Sensor.objects.filter(
                    location__contains=text,
                    location='白居寺车场',
                    value1__gte=temperature.value).count()
                dayan2_location_count = Sensor.objects.filter(
                    location__contains=text,
                    location='大堰',
                    value1__gte=temperature.value).count()
                dayanchechang2_location_count = Sensor.objects.filter(
                    location__contains=text,
                    location='大堰车场',
                    value1__gte=temperature.value).count()
                daping2_location_count = Sensor.objects.filter(
                    location__contains=text,
                    location='大坪',
                    value1__gte=temperature.value).count()

                # 服务器（SESSION）用户信息不为空，显示查询页
                return render(request, 'sensor.html', locals())
        else:
            pass
    else:
        # 服务器（SESSION）用户信息为空，跳转到登录页面
        response = HttpResponseRedirect('/login')
        return response


##############################
# 仪表页
##############################
def meter(request):
    # 获取服务器（SESSION）用户信息
    username = request.session.get('username', None)
    if username:
        # 判断是否为（GET）方式提交
        if request.method == 'GET':
            # 获取提交表单中的设备名称
            name = request.GET['name']
        # 显示仪表页
        return render(request, 'meter.html', locals())
    else:
        # 服务器（SESSION）用户信息为空，跳转到登录页面
        response = HttpResponseRedirect('/login')
        return response


##############################
# 选项页
##############################
def option(request):
    # 获取服务器（SESSION）用户信息
    username = request.session.get('username', None)
    if username:
        # 获取选项数据库中的数据
        temperature = Option.objects.get(name='temperature')
        humidity = Option.objects.get(name='humidity')
        # 显示选项页
        return render(request, 'option.html', locals())
    else:
        # 服务器（SESSION）用户信息为空，跳转到登录页面
        response = HttpResponseRedirect('/login')
        return response


##############################
# 选项数据保存
##############################
def save(request):
    # 获取服务器（SESSION）用户信息
    username = request.session.get('username', None)
    if username:
        # 获取提交表单中的数据
        temperature = request.POST['temperature']
        humidity = request.POST['humidity']
        # 根据温度字段保存到数据库
        option = Option.objects.filter(name='temperature').update(
            value=temperature)
        option = Option.objects.filter(name='humidity').update(value=humidity)
        # 保存到数据库后，跳转到页面
        response = HttpResponseRedirect('/sensor')
        return response
    else:
        # 服务器（SESSION）用户信息为空，跳转到登录页面
        response = HttpResponseRedirect('/login')
        return response


##############################
# 接收传感器数据给数据库
##############################
def add(request):
    # 判断是否为（GET）方式提交
    if request.method == 'GET':
        # 获取提交表单中的温度和湿度
        name = request.GET['name']
        location = request.GET['location']
        value1 = request.GET['value1']  # 表示温度
        value2 = request.GET['value2']  # 表示湿度
        # 添加到数据库
        Sensor.objects.create(
            name=name,
            location=location,
            value1=value1,
            value2=value2,
            create_time=datetime.now(),
            update_time=datetime.now())

        ##############################
        # 判断是否发送警告邮件
        ##############################
        # 获取选项数据库中的数据
        temperature = Option.objects.get(name='temperature')
        humidity = Option.objects.get(name='humidity')
        if value1 >= temperature.value or value2 <= humidity.value:
            # 发送邮件
            response = HttpResponseRedirect('/mail')
            return response
        else:
            pass

        # 格式化为（JSON）数据形式
        data = {
            'name': name,
            'location': location,
            'value1': value1,
            'value2': value2
        }
    # 返回（JSON）数据到页面
    return JsonResponse(data)


##############################
# 传递传感器数据给前端
##############################
def ajax(request):
    # 判断是否为（GET）方式提交
    if request.method == 'GET':
        # 获取提交表单中的设备名称
        name = request.GET['name']
        # 获取传感器数据库中某设备名称的数据并按（ID）编号倒序排列
        data_all_count = Sensor.objects.filter(name__exact=name).order_by('-id')
        # 获取传感器数据库中某设备名称的最后一条数据
        data = Sensor.objects.get(id__exact=data_all_count[0].id)
        # 格式化为（JSON）数据形式
        data = {
            'id': data.id,
            'name': data.name,
            'location': data.location,
            'value1': data.value1,
            'value2': data.value2,
            'value3': data.value3,
            'value4': data.value4,
            'value5': data.value5,
            'create_time': data.create_time,
            'update_time': data.update_time
        }
        # 返回（JSON）数据到页面
        return JsonResponse(data)


##############################
# 发送邮件
##############################
def mail(request):
    ##############################
    # 参数1、邮件标题
    # 参数2、邮件内容
    # 参数3、分为邮件名称和邮件地址
    # 参数4、接收邮件地址
    # 参数5、如果值为False将抛出异常
    ##############################
    # 获取传感器数据库中数据的总数（相当于最后一条数据）
    data_all_count = Sensor.objects.all().count()
    # 查询传感器数据库中最后一条数据
    data = Sensor.objects.get(id__exact=data_all_count)
    # 获取用户数据库中的所有数据
    user = User.objects.all()
    for u in user:
        # 发送邮件
        send_mail(
            '【警告】温度（' + data.value1 + '），湿度（' + data.value2 + '）',
            '【警告】温度（' + data.value1 + '），湿度（' + data.value2 + '），请立即检查。',
            '【警告】<dabolau@163.com>', [u.mail],
            fail_silently=False)
    # 格式化为（JSON）数据形式
    data = {
        'id': data.id,
        'name': data.name,
        'location': data.location,
        'value1': data.value1,
        'value2': data.value2,
        'value3': data.value3,
        'value4': data.value4,
        'value5': data.value5,
        'create_time': data.create_time,
        'update_time': data.update_time
    }
    # 返回（JSON）数据到页面
    return JsonResponse(data)


##############################
# 发送微信
##############################
def wechat(request):
    # 获取传感器数据库中数据的总数（相当于最后一条数据）
    data_all_count = Sensor.objects.all().count()
    # 查询传感器数据库中最后一条数据
    data = Sensor.objects.get(id__exact=data_all_count)
    # 获取用户数据库中的所有数据
    user = User.objects.all()


    # 格式化为（JSON）数据形式
    data = {
        'id': data.id,
        'name': data.name,
        'location': data.location,
        'value1': data.value1,
        'value2': data.value2,
        'value3': data.value3,
        'value4': data.value4,
        'value5': data.value5,
        'create_time': data.create_time,
        'update_time': data.update_time
    }
    # 返回（JSON）数据到页面
    return JsonResponse(data)
