from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User


#首页
def home(request):
    return render(request, 'home.html', locals())


# 主要页面
def main(request):
    user = request.user
    if str(user) == 'AnonymousUser':
        return HttpResponseRedirect('login')
    else:
        return render(request, 'main.html', locals())


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', locals())
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('main')
        else:
            return render(request, 'login.html', locals())


# 注销
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('login')


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', locals())
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        verifypassword = request.POST.get('verifypassword')
        try:
            User.objects.get(username=username)
            return HttpResponse('用户存在')
        except User.DoesNotExist:
            if username != '' and email != '' and password != '' and password == verifypassword:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )
                user.save()
                return HttpResponse('注册成功')
            else:
                return HttpResponseRedirect('register')


# 修改密码
def changepassword(request):
    if request.method == 'GET':
        return render(request, 'changepassword.html', locals())
    else:
        username = request.POST.get('username')
        oldpassword = request.POST.get('oldpassword')
        password = request.POST.get('password')
        verifypassword = request.POST.get('verifypassword')
        user = auth.authenticate(username=username, password=oldpassword)
        if user is not None:
            if password != '' and password == verifypassword:
                user = User.objects.get(username=username)
                user.set_password(password)
                user.save()
                return HttpResponse('修改成功')
        else:
            return HttpResponseRedirect('changepassword')


# 重置
def reset(request):
    if request.method == 'GET':
        return render(request, 'reset.html', locals())
    else:
        pass
