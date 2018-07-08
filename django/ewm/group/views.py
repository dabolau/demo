from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import auth
from django.contrib.auth.models import User
from django import forms
from home.models import *
from group.models import *

import qrcode


###
# 班组信息模型表单
###
class Group_ModelForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'group_photo':
            forms.widgets.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': '例如：班组照片',
            }),
            'group_name':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：白居寺车场通信工班',
            }),
            'group_location':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：白居寺车场运用库三零一室',
            }),
            'group_phone':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：68004925',
            }),
            'group_introduction':
            forms.widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '例如：同心协力，乘风破浪',
            }),
            'group_member':
            forms.widgets.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': '例如：班组成员',
            }),
            'group_equipment':
            forms.widgets.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': '例如：班组设备',
            }),
            'group_other_information':
            forms.widgets.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': '例如：其他附件',
            }),
        }


###
# 首页
###
@login_required(login_url='/account/login')
def group(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        name = request.GET.get('name')
        if name == None:
            return HttpResponseRedirect('/group/?name=')
        obj_all = Group.objects.filter(
            group_name__contains=name).order_by('-id')
        # 查询分页
        paginator = Paginator(obj_all, 10)  # 每页显示一条数据
        page = request.GET.get('page')
        try:
            obj = paginator.page(page)
        except PageNotAnInteger:
            obj = paginator.page(1)  # 如果页面不是整数跳到第一页
        except EmptyPage:
            obj = paginator.page(paginator.num_pages)  # 如果页面超出最大范围跳到最后一页
        return render(request, 'group.html', locals())


###
# 详情
###
def group_detail(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        id = request.GET.get('id')
        obj = Group.objects.filter(id=id).first()
        if not obj:
            return HttpResponse('detail not have obj')
        if id is not None:
            host = request.META['HTTP_HOST']
            qr = qrcode.make(
                'http://' + host + '/group/group_detail/?id=' + id)
            qr.save('static/qrcode/group/' + id + '.png')
        ###
        # 获取group_member多对多中的全部数据
        ###
        memberobj = Group.objects.get(id=id).group_member.all()
        ###
        # 获取group_equipment多对多中的全部数据
        ###
        equipmentobj = Group.objects.get(id=id).group_equipment.all()
        ###
        # 获取group_other_information多对多中的全部数据
        ###
        fileobj = Group.objects.get(id=id).group_other_information.all()
        ###
        # 获取group_photo多对多中的全部数据
        ###
        fileobjphoto = Group.objects.get(id=id).group_photo.all()
        return render(request, 'group_detail.html', locals())


###
# 添加
###
@login_required(login_url='/account/login')
@permission_required(perm='group.add_group', login_url='/group')
def group_add(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        GMF = Group_ModelForm()
        return render(request, 'group_add.html', locals())
    else:
        GMF = Group_ModelForm(
            request.POST,
            request.FILES,
        )
        if GMF.is_valid():
            GMF.save()
        return HttpResponseRedirect('/group/')


###
# 编辑
###
@login_required(login_url='/account/login')
@permission_required(perm='group.change_group', login_url='/group')
def group_change(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        id = request.GET.get('id')
        obj = Group.objects.filter(id=id).first()
        if not obj:
            return HttpResponse('change not have obj')
        GMF = Group_ModelForm(instance=obj, )
        return render(request, 'group_change.html', locals())
    else:
        id = request.GET.get('id')
        obj = Group.objects.filter(id=id).first()
        GMF = Group_ModelForm(
            request.POST,
            request.FILES,
            instance=obj,
        )
        if GMF.is_valid():
            GMF.save()
        return HttpResponseRedirect('/group/')


###
# 删除
###
@login_required(login_url='/account/login')
@permission_required(perm='group.delete_group', login_url='/group')
def group_delete(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        id = request.GET.get('id')
        obj = Group.objects.filter(id=id).first()
        if not obj:
            return HttpResponse('delete not have obj')
        return render(request, 'group_delete.html', locals())
    else:
        id = request.GET.get('id')
        obj = Group.objects.filter(id=id).first()
        Group.objects.filter(id=id).delete()
        return HttpResponseRedirect('/group/')
