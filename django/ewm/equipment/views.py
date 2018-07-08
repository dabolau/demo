from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import auth
from django.contrib.auth.models import User
from django import forms
from home.models import *
from equipment.models import *

import qrcode


###
# 设备履历模型表单
###
class Equipment_ModelForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'
        widgets = {
            'equipment_photo':
            forms.widgets.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': '例如：设备照片',
            }),
            'equipment_name':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：双电源切换柜',
            }),
            'manufacturer_name':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：成都信号工厂',
            }),
            'model_specification':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：GGD-GB7521',
            }),
            'equipment_location':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：三号线信号电源室',
            }),
            'enable_date':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：20110510',
            }),
            ###
            # 上传文件样式
            ###
            # 'html_file':
            # forms.widgets.FileInput(attrs={
            #     'class': 'form-control',
            # }),
            # 'other_file':
            # forms.widgets.FileInput(attrs={
            #     'class': 'form-control',
            # }),
            'other_information':
            forms.widgets.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': '例如：其他附件',
            }),
        }


###
# 首页
###
@login_required(login_url='/account/login')
def equipment(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        name = request.GET.get('name')
        if name == None:
            return HttpResponseRedirect('/equipment/?name=')
        obj_all = Equipment.objects.filter(
            equipment_name__contains=name).order_by('-id')
        # 查询分页
        paginator = Paginator(obj_all, 10)  # 每页显示一条数据
        page = request.GET.get('page')
        try:
            obj = paginator.page(page)
        except PageNotAnInteger:
            obj = paginator.page(1)  # 如果页面不是整数跳到第一页
        except EmptyPage:
            obj = paginator.page(paginator.num_pages)  # 如果页面超出最大范围跳到最后一页
        return render(request, 'equipment.html', locals())


###
# 详情
###
def equipment_detail(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        id = request.GET.get('id')
        obj = Equipment.objects.filter(id=id).first()
        if not obj:
            return HttpResponse('detail not have obj')
        if id is not None:
            host = request.META['HTTP_HOST']
            qr = qrcode.make(
                'http://' + host + '/equipment/equipment_detail/?id=' + id)
            qr.save('static/qrcode/equipment/' + id + '.png')
        ###
        # 获取other_information多对多中的全部数据
        ###
        fileobj = Equipment.objects.get(id=id).other_information.all()
        ###
        # 获取equipment_photo多对多中的全部数据
        ###
        fileobjphoto = Equipment.objects.get(id=id).equipment_photo.all()
        return render(request, 'equipment_detail.html', locals())


###
# 添加
###
@login_required(login_url='/account/login')
@permission_required(perm='equipment.add_equipment', login_url='/equipment')
def equipment_add(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        EMF = Equipment_ModelForm()
        return render(request, 'equipment_add.html', locals())
    else:
        EMF = Equipment_ModelForm(
            request.POST,
            request.FILES,
        )
        if EMF.is_valid():
            EMF.save()
        return HttpResponseRedirect('/equipment/')


###
# 编辑
###
@login_required(login_url='/account/login')
@permission_required(perm='equipment.change_equipment', login_url='/equipment')
def equipment_change(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        id = request.GET.get('id')
        obj = Equipment.objects.filter(id=id).first()
        if not obj:
            return HttpResponse('change not have obj')
        EMF = Equipment_ModelForm(instance=obj, )
        return render(request, 'equipment_change.html', locals())
    else:
        id = request.GET.get('id')
        obj = Equipment.objects.filter(id=id).first()
        EMF = Equipment_ModelForm(
            request.POST,
            request.FILES,
            instance=obj,
        )
        if EMF.is_valid():
            EMF.save()
        return HttpResponseRedirect('/equipment/')


###
# 删除
###
@login_required(login_url='/account/login')
@permission_required(perm='equipment.delete_equipment', login_url='/equipment')
def equipment_delete(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        id = request.GET.get('id')
        obj = Equipment.objects.filter(id=id).first()
        if not obj:
            return HttpResponse('delete not have obj')
        return render(request, 'equipment_delete.html', locals())
    else:
        id = request.GET.get('id')
        obj = Equipment.objects.filter(id=id).first()
        Equipment.objects.filter(id=id).delete()
        return HttpResponseRedirect('/equipment/')
