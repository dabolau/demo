##############################
# 版权归作者所有
# 作者：刘毅
# 日期：20170930
# 版本号：1.0
##############################
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from home.models import *
from datetime import *


# 首页
def home(request):
    # 从首页跳转到登录页
    # response = HttpResponseRedirect('/login')
    # return response
    # 显示首页
    # return render(request, 'home.html', locals())
    # 获取服务器（SESSION）用户信息
    username = request.session.get('username', None)
    if username:
        # 服务器（SESSION）用户信息不为空，跳转到产品页面
        response = HttpResponseRedirect('/product')
        return response
    else:
        # 服务器（SESSION）用户信息为空，跳转到登录页面
        response = HttpResponseRedirect('/login')
        return response


# 登录
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
            response = HttpResponseRedirect('/product')
            return response
        else:
            # 如果用户和密码不相同，返回登录失败的信息
            message = '登录失败，用户或密码错误。'
    else:
        pass
    # 显示登录页
    return render(request, 'login.html', locals())


# 注销
def logout(request):
    try:
        # 删除服务器（SESSION）
        del request.session['username']
    except KeyError:
        pass
    # 跳转到登录页
    response = HttpResponseRedirect('/login')
    return response


# 产品
def product(request):
    # # 获取服务器（SESSION）用户信息
    # username = request.session.get('username', None)
    # if username:

    #     if request.method == 'GET':
    #         product_all = Product.objects.all().order_by('-create_time')
    #         paginator = Paginator(product_all, 10)  # 每页显示一条数据
    #         page = request.GET.get('page')
    #         try:
    #             product = paginator.page(page)
    #         except PageNotAnInteger:
    #             product = paginator.page(1)  # 如果页面不是整数跳到第一页
    #         except EmptyPage:
    #             product = paginator.page(
    #                 paginator.num_pages)  # 如果页面超出最大范围跳到最后一页

    #     # 服务器（SESSION）用户信息不为空，显示页面
    #     return render(request, 'product.html', locals())
    # else:
    #     # 服务器（SESSION）用户信息为空，跳转到登录页面
    #     response = HttpResponseRedirect('/login')
    #     return response

    # 获取服务器（SESSION）用户信息
    username = request.session.get('username', None)
    if username:

        # 获取表单中的信息
        if request.method == 'GET':
            text = request.GET.get('text')
            # 判断表单获取的信息为空，跳转到产品页
            if text == None:
                response = HttpResponseRedirect('/product?text=')
                return response
            # 查询表单中的信息
            product_all = Product.objects.filter(
                name__contains=text).order_by('-create_time')
            # 查询分页
            paginator = Paginator(product_all, 10)  # 每页显示一条数据
            page = request.GET.get('page')
            try:
                product = paginator.page(page)
            except PageNotAnInteger:
                product = paginator.page(1)  # 如果页面不是整数跳到第一页
            except EmptyPage:
                product = paginator.page(
                    paginator.num_pages)  # 如果页面超出最大范围跳到最后一页

            # 输出图表中总计，好，坏数目
            all_count = Product.objects.filter(name__contains=text).count()
            ok_count = Product.objects.filter(
                name__contains=text, state='好').count()
            no_count = Product.objects.filter(
                name__contains=text, state='坏').count()
            # 输出图表中总计，车间、白居寺、白居寺车场、大堰、大堰车场、大坪
            all_location_count = Product.objects.filter(
                name__contains=text).count()
            chejian_location_count = Product.objects.filter(
                name__contains=text, location='车间').count()
            baijusi_location_count = Product.objects.filter(
                name__contains=text, location='白居寺').count()
            baijusichechang_location_count = Product.objects.filter(
                name__contains=text, location='白居寺车场').count()
            dayan_location_count = Product.objects.filter(
                name__contains=text, location='大堰').count()
            dayanchechang_location_count = Product.objects.filter(
                name__contains=text, location='大堰车场').count()
            daping_location_count = Product.objects.filter(
                name__contains=text, location='大坪').count()

        else:
            pass
        # 服务器（SESSION）用户信息不为空，显示查询页
        return render(request, 'product.html', locals())
    else:
        # 服务器（SESSION）用户信息为空，跳转到登录页面
        response = HttpResponseRedirect('/login')
        return response


# 产品添加
def add(request):
    # 获取服务器（SESSION）用户信息
    username = request.session.get('username', None)
    if username:
        # 判断是否为安全（POST）方式提交
        if request.method == 'POST':
            # 获取提交表单中的数据
            name = request.POST['name']
            location = request.POST['location']
            state = request.POST['state']
            # 判断表单中的内容是否为空，为空返回错误信息
            if name == '' or location == '' or state == '':
                message = '添加失败，内容填写不完整。'
            else:
                # 添加到数据库
                Product.objects.create(name=name, location=location, state=state,
                                       create_time=datetime.now(), update_time=datetime.now())
                # 添加到数据库后，跳转到产品页
                response = HttpResponseRedirect('/product')
                return response
        else:
            pass
        return render(request, 'add.html', locals())
    else:
        # 服务器（SESSION）用户信息为空，跳转到登录页面
        response = HttpResponseRedirect('/login')
        return response


# 产品编辑
def edit(request):
    # 获取服务器（SESSION）用户信息
    username = request.session.get('username', None)
    if username:
        # 获取表单中的编号（ID）
        if request.method == 'GET':
            id = request.GET.get('id')

            if id == None:
                # 添加到数据库后，跳转到产品页
                response = HttpResponseRedirect('/product')
                return response
            else:
                edit = Product.objects.filter(id__exact=id)

        # 服务器（SESSION）用户信息不为空，显示页面
        return render(request, 'edit.html', locals())
    else:
        # 服务器（SESSION）用户信息为空，跳转到登录页面
        response = HttpResponseRedirect('/login')
        return response


# 产品保存
def save(request):
    # 获取服务器（SESSION）用户信息
    username = request.session.get('username', None)
    if username:
        if request.method == 'POST':
            # 获取提交表单中的数据
            id = request.POST['id']
            name = request.POST['name']
            location = request.POST['location']
            state = request.POST['state']
            # 根据编号（ID）保存到数据库
            product = Product.objects.filter(id=id).update(
                name=name, location=location, state=state, update_time=datetime.now())
            # 保存到数据库后，跳转到产品页
            response = HttpResponseRedirect('/product')
            return response
        else:
            # 保存到数据库后，跳转到产品页
            response = HttpResponseRedirect('/product')
            return response
    else:
        # 服务器（SESSION）用户信息为空，跳转到登录页面
        response = HttpResponseRedirect('/login')
        return response


# 产品删除
def delete(request):
    # 获取服务器（SESSION）用户信息
    username = request.session.get('username', None)
    if username:
        if request.method == 'GET':
            # 获取提交表单中的数据
            id = request.GET.get('id')
            # 根据编号（ID）删除数据库的相关内容
            product = Product.objects.filter(id=id).delete()
            # 删除数据库后，跳转到产品页
            response = HttpResponseRedirect('/product')
            return response
        else:
            # 删除数据库后，跳转到产品页
            response = HttpResponseRedirect('/product')
            return response
    else:
        # 服务器（SESSION）用户信息为空，跳转到登录页面
        response = HttpResponseRedirect('/login')
        return response


# 404页面，开启需要将配置修改为（DEBUG=False）
def page_not_found(request):
    return render(request, '404.html', locals())


# 500页面，开启需要将配置修改为（DEBUG=False）
def page_error(request):
    return render(request, '500.html', locals())
