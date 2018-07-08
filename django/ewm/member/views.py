from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import auth
from django.contrib.auth.models import User
from django import forms
from home.models import *
from member.models import *

import qrcode


###
# 员工信息模型表单
###
class Member_ModelForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        widgets = {
            'member_photo':
            forms.widgets.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': '例如：员工照片',
            }),
            'member_number':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：18152',
            }),
            'member_name':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：刘毅5',
            }),
            'member_sex':
            forms.widgets.Select(attrs={
                'class': 'form-control',
                'placeholder': '例如：男',
            }),
            'member_birthday':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：19841109',
            }),
            'entry_time':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：20170718',
            }),
            'member_company':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：重庆市轨道交通（集团）有限公司',
            }),
            'member_department':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：通号维保部',
            }),
            'member_position':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：通信维修工',
            }),
            'member_level':
            forms.widgets.Select(attrs={
                'class': 'form-control',
                'placeholder': '例如：中三',
            }),
            'political_status':
            forms.widgets.Select(attrs={
                'class': 'form-control',
                'placeholder': '例如：群众',
            }),
            'member_phone':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：13548332689',
            }),
            'member_email':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：dabolau@qq.com',
            }),
            'member_introduction':
            forms.widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '例如：勇做轨道螺丝钉',
            }),
            'member_other':
            forms.widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '例如：吃葡萄不吐葡萄皮，不吃葡萄倒吐葡萄皮',
            }),
        }


###
# 首页
###
@login_required(login_url='/account/login')
def member(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        name = request.GET.get('name')
        if name == None:
            return HttpResponseRedirect('/member/?name=')
        obj_all = Member.objects.filter(
            member_name__contains=name).order_by('-id')
        # 查询分页
        paginator = Paginator(obj_all, 10)  # 每页显示一条数据
        page = request.GET.get('page')
        try:
            obj = paginator.page(page)
        except PageNotAnInteger:
            obj = paginator.page(1)  # 如果页面不是整数跳到第一页
        except EmptyPage:
            obj = paginator.page(paginator.num_pages)  # 如果页面超出最大范围跳到最后一页
        return render(request, 'member.html', locals())


###
# 详情
###
def member_detail(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        id = request.GET.get('id')
        obj = Member.objects.filter(id=id).first()
        if not obj:
            return HttpResponse('detail not have obj')
        if id is not None:
            host = request.META['HTTP_HOST']
            qr = qrcode.make(
                'http://' + host + '/member/member_detail/?id=' + id)
            qr.save('static/qrcode/member/' + id + '.png')
        ###
        # 获取多对多中的全部数据
        ###
        fileobjphoto = Member.objects.get(id=id).member_photo.all()
        return render(request, 'member_detail.html', locals())


###
# 添加
###
@login_required(login_url='/account/login')
@permission_required(perm='member.add_member', login_url='/member')
def member_add(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        MMF = Member_ModelForm()
        return render(request, 'member_add.html', locals())
    else:
        MMF = Member_ModelForm(
            request.POST,
            request.FILES,
        )
        if MMF.is_valid():
            MMF.save()
        return HttpResponseRedirect('/member/')


###
# 编辑
###
@login_required(login_url='/account/login')
@permission_required(perm='member.change_member', login_url='/member')
def member_change(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        id = request.GET.get('id')
        obj = Member.objects.filter(id=id).first()
        if not obj:
            return HttpResponse('change not have obj')
        MMF = Member_ModelForm(instance=obj, )
        return render(request, 'member_change.html', locals())
    else:
        id = request.GET.get('id')
        obj = Member.objects.filter(id=id).first()
        MMF = Member_ModelForm(
            request.POST,
            request.FILES,
            instance=obj,
        )
        if MMF.is_valid():
            MMF.save()
        return HttpResponseRedirect('/member/')


###
# 删除
###
@login_required(login_url='/account/login')
@permission_required(perm='member.delete_member', login_url='/member')
def member_delete(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        id = request.GET.get('id')
        obj = Member.objects.filter(id=id).first()
        if not obj:
            return HttpResponse('delete not have obj')
        return render(request, 'member_delete.html', locals())
    else:
        id = request.GET.get('id')
        obj = Member.objects.filter(id=id).first()
        Member.objects.filter(id=id).delete()
        return HttpResponseRedirect('/member/')
