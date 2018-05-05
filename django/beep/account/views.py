from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth


###
# 用户首页视图
###
def account(request):
    user = request.user
    return HttpResponseRedirect('/account/login')


###
# 用户登录视图
###
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', locals())
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = '登录失败，用户或密码错误。'
            return render(request, 'login.html', locals())


###
# 用户注销视图
###
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/account/login')
