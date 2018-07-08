from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import auth
from django.contrib.auth.models import User
from django import forms
from home.models import *


###
# 用户信息模型表单
###
class User_ModelForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'user_permissions',
        ]
        widgets = {
            'username':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：18152',
            }),
            'password':
            forms.widgets.TextInput(
                attrs={
                    'class':
                    'form-control',
                    'placeholder':
                    '例如：pbkdf2_sha256$100000$ghsQivyQza6p$SocvxPy7oRP0znB3R2c0BzXaedJfNugBCviDWSC5b6k=',
                }),
            'email':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：dabolau@qq.com',
            }),
            'first_name':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：毅5',
            }),
            'last_name':
            forms.widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例如：刘',
            }),
            'user_permissions':
            forms.widgets.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': '例如：选择需要控制的权限',
            }),
        }


###
# 首页
###
@login_required(login_url='/account/login')
def user(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        name = request.GET.get('name')
        if name == None:
            return HttpResponseRedirect('/user/?name=')
        obj_all = User.objects.filter(
            username__contains=name,
            is_superuser=False,
        ).order_by('-id')
        # 查询分页
        paginator = Paginator(obj_all, 10)  # 每页显示一条数据
        page = request.GET.get('page')
        try:
            obj = paginator.page(page)
        except PageNotAnInteger:
            obj = paginator.page(1)  # 如果页面不是整数跳到第一页
        except EmptyPage:
            obj = paginator.page(paginator.num_pages)  # 如果页面超出最大范围跳到最后一页
        return render(request, 'user.html', locals())


###
# 添加
###
@login_required(login_url='/account/login')
@permission_required(perm='auth.add_user', login_url='/user')
def user_add(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        UMF = User_ModelForm()
        return render(request, 'user_add.html', locals())
    else:
        UMF = User_ModelForm(
            request.POST,
            request.FILES,
        )
        if UMF.is_valid():
            UMF.save()
        return HttpResponseRedirect('/user/')


###
# 编辑
###
@login_required(login_url='/account/login')
@permission_required(perm='auth.change_user', login_url='/user')
def user_change(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        id = request.GET.get('id')
        obj = User.objects.filter(id=id).first()
        if not obj:
            return HttpResponse('change not have obj')
        UMF = User_ModelForm(instance=obj, )
        return render(request, 'user_change.html', locals())
    else:
        id = request.GET.get('id')
        obj = User.objects.filter(id=id).first()
        UMF = User_ModelForm(
            request.POST,
            request.FILES,
            instance=obj,
        )
        if UMF.is_valid():
            UMF.save()
        return HttpResponseRedirect('/user/')


###
# 删除
###
@login_required(login_url='/account/login')
@permission_required(perm='auth.delete_user', login_url='/user')
def user_delete(request):
    if request.method == 'GET':
        ###
        # 网站状态控制，可打开和关闭网站
        ###
        homeobj = Home.objects.filter(web_name='网站状态', web_status='打开').first()
        if not homeobj:
            return HttpResponseRedirect('/note/')

        id = request.GET.get('id')
        obj = User.objects.filter(id=id).first()
        if not obj:
            return HttpResponse('delete not have obj')
        return render(request, 'user_delete.html', locals())
    else:
        id = request.GET.get('id')
        obj = User.objects.filter(id=id).first()
        User.objects.filter(id=id).delete()
        return HttpResponseRedirect('/user/')