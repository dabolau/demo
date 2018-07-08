from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import auth
from django.contrib.auth.models import User
from django import forms
from home.models import *
from file.models import *

import qrcode


###
# 附件信息模型表单
###
class File_ModelForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
        widgets = {
            'file_name':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：白居寺通信工班照片'
            }),
            'file_tag':
            forms.widgets.Select(attrs={
                'class': 'form-control',
                'placeholder': '例如：班组照片'
            }),
            ###
            # 上传文件样式
            ###
            # 'file_upload':
            # forms.widgets.FileInput(attrs={
            #     'class': 'form-control',
            # }),
        }


###
# 首页
###
@login_required(login_url='/account/login')
def file(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        name = request.GET.get('name')
        if name == None:
            return HttpResponseRedirect('/file/?name=')
        obj_all = File.objects.filter(file_name__contains=name).order_by('-id')
        # 查询分页
        paginator = Paginator(obj_all, 10)  # 每页显示一条数据
        page = request.GET.get('page')
        try:
            obj = paginator.page(page)
        except PageNotAnInteger:
            obj = paginator.page(1)  # 如果页面不是整数跳到第一页
        except EmptyPage:
            obj = paginator.page(paginator.num_pages)  # 如果页面超出最大范围跳到最后一页
        return render(request, 'file.html', locals())


###
# 详情
###
def file_detail(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        id = request.GET.get('id')
        obj = File.objects.filter(id=id).first()
        if not obj:
            return HttpResponse('detail not have obj')
        if id is not None:
            host = request.META['HTTP_HOST']
            qr = qrcode.make('http://' + host + '/file/file_detail/?id=' + id)
            qr.save('static/qrcode/file/' + id + '.png')
        return render(request, 'file_detail.html', locals())


###
# 添加
###
@login_required(login_url='/account/login')
@permission_required(perm='file.add_file', login_url='/file')
def file_add(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        FMF = File_ModelForm()
        return render(request, 'file_add.html', locals())
    else:
        FMF = File_ModelForm(
            request.POST,
            request.FILES,
        )
        if FMF.is_valid():
            FMF.save()
        return HttpResponseRedirect('/file/')


###
# 编辑
###
@login_required(login_url='/account/login')
@permission_required(perm='file.change_file', login_url='/file')
def file_change(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        id = request.GET.get('id')
        obj = File.objects.filter(id=id).first()
        if not obj:
            return HttpResponse('change not have obj')
        FMF = File_ModelForm(instance=obj, )
        return render(request, 'file_change.html', locals())
    else:
        id = request.GET.get('id')
        obj = File.objects.filter(id=id).first()
        FMF = File_ModelForm(
            request.POST,
            request.FILES,
            instance=obj,
        )
        if FMF.is_valid():
            FMF.save()
        return HttpResponseRedirect('/file/')


###
# 删除
###
@login_required(login_url='/account/login')
@permission_required(perm='file.delete_file', login_url='/file')
def file_delete(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        id = request.GET.get('id')
        obj = File.objects.filter(id=id).first()
        if not obj:
            return HttpResponse('delete not have obj')
        return render(request, 'file_delete.html', locals())
    else:
        id = request.GET.get('id')
        obj = File.objects.filter(id=id).first()
        File.objects.filter(id=id).delete()
        return HttpResponseRedirect('/file/')
