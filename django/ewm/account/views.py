from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django import forms
from django.core.mail import send_mail

from random import randint


###
# 首页
###
def account(request):
    return HttpResponseRedirect('/account/login/')


###
# 登录表单
###
class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=5,
        max_length=128,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '用户名',
            }, ),
    )
    password = forms.CharField(
        min_length=8,
        max_length=128,
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '密码',
            }, ),
    )


###
# 登录
###
def login(request):
    if request.method == 'GET':
        lf = LoginForm()
        return render(request, 'login.html', locals())
    else:
        lf = LoginForm(request.POST)
        if lf.is_valid():
            username = lf.cleaned_data['username']
            password = lf.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                message = '登录成功'
                return HttpResponseRedirect('/main/')
            else:
                message = '用户名或密码错误'
        return render(request, 'login.html', locals())


###
# 注册表单
###
class RegisterForm(forms.Form):
    username = forms.CharField(
        min_length=5,
        max_length=128,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '用户名',
            }, ),
    )
    email = forms.EmailField(
        min_length=4,
        max_length=254,
        label='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '邮件地址',
            }, ),
    )
    password = forms.CharField(
        min_length=8,
        max_length=128,
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '密码',
            }, ),
    )


###
# 注册
###
def register(request):
    if request.method == 'GET':
        rf = RegisterForm()
        return render(request, 'register.html', locals())
    else:
        rf = RegisterForm(request.POST)
        if rf.is_valid():
            username = rf.cleaned_data['username']
            email = rf.cleaned_data['email']
            password = rf.cleaned_data['password']
            have_user = User.objects.filter(username=username).first()
            if have_user:
                message = '用户名已存在'
            else:
                have_email = User.objects.filter(email=email).first()
                if have_email:
                    message = '邮件地址已存在'
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                    )
                    message = '注册成功'
        else:
            message = '邮件地址格式错误'
        return render(request, 'register.html', locals())


###
# 修改密码表单
###
class ChangepasswordForm(forms.Form):
    username = forms.CharField(
        min_length=5,
        max_length=128,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '用户名',
            }, ),
    )
    password = forms.CharField(
        min_length=8,
        max_length=128,
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '旧的密码',
            }, ),
    )
    password2 = forms.CharField(
        min_length=8,
        max_length=128,
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '新的密码',
            }, ),
    )
    password3 = forms.CharField(
        min_length=8,
        max_length=128,
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '重复密码',
            }, ),
    )


###
# 修改密码
###
def changepassword(request):
    if request.method == 'GET':
        cf = ChangepasswordForm()
        return render(request, 'changepassword.html', locals())
    else:
        cf = ChangepasswordForm(request.POST)
        if cf.is_valid():
            print(cf.cleaned_data)
            username = cf.cleaned_data['username']
            password = cf.cleaned_data['password']
            password2 = cf.cleaned_data['password2']
            password3 = cf.cleaned_data['password3']
            user = auth.authenticate(username=username, password=password)
            if user:
                if password2 == password3:
                    user = User.objects.filter(username=username).first()
                    user.set_password(password2)
                    user.save()
                    message = '修改成功'
                else:
                    message = '新的密码和重复密码不相同'
            else:
                message = '用户名或旧的密码错误'
        return render(request, 'changepassword.html', locals())


###
# 找回密码表单
###
class GetpasswordForm(forms.Form):
    username = forms.CharField(
        min_length=5,
        max_length=128,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '用户名',
            }, ),
    )
    email = forms.EmailField(
        min_length=4,
        max_length=254,
        label='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '邮件地址',
            }, ),
    )


###
# 找回密码
###
def getpassword(request):
    if request.method == 'GET':
        gf = GetpasswordForm()
        return render(request, 'getpassword.html', locals())
    else:
        gf = GetpasswordForm(request.POST)
        if gf.is_valid():
            username = gf.cleaned_data['username']
            email = gf.cleaned_data['email']
            password = randint(10000000, 99999999)
            user = User.objects.filter(
                username=username,
                email=email,
            ).first()
            if user:
                user.set_password(password)
                user.save()
                print(user.username, user.password, password)
                ###
                # 找回密码发送邮件功能只在linux系统下正常工作，需要配合settings.py文件中的邮件信息使用
                ###
                send_mail(
                    subject='找到您的信息',
                    message='您的帐号：[' + user.username + ']，密码：[' +
                    str(password) + ']，请及时修改。',
                    from_email='信息<dabolau@163.com>',
                    recipient_list=[user.email],
                )
                message = '发送成功'
            elif user == None:
                message = '用户名和邮件地址不匹配'
            else:
                message = '未知错误'
        else:
            message = '邮件地址格式错误'
        return render(request, 'getpassword.html', locals())


###
# 注销
###
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/account/')
