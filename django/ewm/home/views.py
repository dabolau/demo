from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import *

import qrcode


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
# 入口界面，显示滚动图片
###
def home(request):
    ###
    # 页面显示
    ###
    return render(request, 'home.html', locals())


###
# 首页
###
def main(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        obj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not obj:
            return HttpResponseRedirect('/note/')
        ###
        # 生成二维码图片并保存
        ###
        host = request.META['HTTP_HOST']
        qr = qrcode.make('http://' + host)
        qr.save('static/qrcode/home/home.png')
        ###
        # 页面显示
        ###
        return render(request, 'home_main.html', locals())


###
# 问题反馈
###
def bug(request):
    if request.method == 'GET':
        ###
        # 页面显示
        ###
        return render(request, 'home_bug.html', locals())


###
# 网站信息
###
def note(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        if name == None:
            return HttpResponseRedirect('/note/?name=网站公告')
        obj = Home.objects.filter(web_name=name, web_status='打开').first()
        if not obj:
            return HttpResponse('note not have obj')
        ###
        # 页面显示
        ###
        return render(request, 'home_note.html', locals())