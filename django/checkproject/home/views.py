from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django import forms
from home.models import *


# 首页视图
@login_required(login_url='/account/')
def home(request):
    return render(request, 'home.html', locals())


############
#步骤
############


#与数据库模型绑定的表单（步骤）
class Bjs_base_step_ModelForm(forms.ModelForm):
    class Meta:
        model = Bjs_base_step
        fields = '__all__'
        # exclude = ['check_man']


#步骤（开始）
@login_required(login_url='/account/')
@permission_required(perm='home.add_bjs_base_step', login_url='/home/')
def add_bjs_base_step_start(request):
    if request.method == 'GET':
        user = request.user
        obj = Bjs_base_step.objects.filter(check_man_id=user.id).first()
        if not obj:
            return render(request, 'add_bjs_base_step_start.html', locals())
        else:
            return HttpResponse('have obj')
    else:
        user = request.user
        # get = Bjs_base_step.objects.create(check_man_id=user.id)
        # print(get.id)
        obj = Bjs_base_step.objects.filter(id=get.id).first()
        print(obj)
        return HttpResponseRedirect(
            '/home/add_bjs_base_step_end?id=' + str(obj.id))


#步骤（结束）
@login_required(login_url='/account/')
@permission_required(perm='home.add_bjs_base_step', login_url='/home/')
def add_bjs_base_step_end(request):
    id = request.GET.get('id')
    obj = Bjs_base_step.objects.filter(id=id).first()
    if not obj:
        return HttpResponse('edit post not have obj')
    if request.method == 'GET':
        BBSMF = Bjs_base_step_ModelForm(instance=obj, )
        return render(request, 'add_bjs_base_step_end.html', locals())
    else:
        BBSMF = Bjs_base_step_ModelForm(
            request.POST,
            instance=obj,
        )
        if BBSMF.is_valid():
            BBSMF.save()
        return HttpResponse('add post')


############
#双电源切换柜
############


#与数据库模型绑定的表单（双电源切换柜）
class Bjs_base_dual_power_switching_ModelForm(forms.ModelForm):
    class Meta:
        model = Bjs_base_dual_power_switching
        fields = '__all__'


#双电源切换柜（列表）
@login_required(login_url='/account/')
def list_bjs_base_dual_power_switching(request):
    obj = Bjs_base_dual_power_switching.objects.all()
    return render(request, 'list_bjs_base_dual_power_switching.html', locals())


#双电源切换柜（详情）
@login_required(login_url='/account/')
def page_bjs_base_dual_power_switching(request):
    obj = Bjs_base_dual_power_switching.objects.all()
    return render(request, 'page_bjs_base_dual_power_switching.html', locals())


#双电源切换柜（添加）
@login_required(login_url='/account/')
@permission_required(
    perm='home.add_bjs_base_dual_power_switching', login_url='/home/')
def add_bjs_base_dual_power_switching(request):
    if request.method == 'GET':
        BBDPSMF = Bjs_base_dual_power_switching_ModelForm()
        return render(request, 'add_bjs_base_dual_power_switching.html',
                      locals())
    else:
        BBDPSMF = Bjs_base_dual_power_switching_ModelForm(request.POST)
        if BBDPSMF.is_valid():
            BBDPSMF.save()
        return HttpResponse('add post')


#双电源切换柜（编辑）
@login_required(login_url='/account/')
@permission_required(
    perm='home.change_bjs_base_dual_power_switching', login_url='/home/')
def change_bjs_base_dual_power_switching(request):
    id = request.GET.get('id')
    obj = Bjs_base_dual_power_switching.objects.filter(id=id).first()
    if not obj:
        return HttpResponse('edit post not have obj')
    if request.method == 'GET':
        BBDPSMF = Bjs_base_dual_power_switching_ModelForm(instance=obj, )
        return render(request, 'change_bjs_base_dual_power_switching.html',
                      locals())
    else:
        BBDPSMF = Bjs_base_dual_power_switching_ModelForm(
            request.POST,
            instance=obj,
        )
        if BBDPSMF.is_valid():
            BBDPSMF.save()
        return HttpResponse('edit post')


#双电源切换柜（删除）
@login_required(login_url='/account/')
@permission_required(
    perm='home.delete_bjs_base_dual_power_switching', login_url='/home/')
def delete_bjs_base_dual_power_switching(request):
    id = request.GET.get('id')
    obj = Bjs_base_dual_power_switching.objects.filter(id=id).first()
    if not obj:
        return HttpResponse('delete post not have obj')
    if request.method == 'GET':
        BBDPSMF = Bjs_base_dual_power_switching_ModelForm(instance=obj, )
        return render(request, 'delete_bjs_base_dual_power_switching.html',
                      locals())
    else:
        Bjs_base_dual_power_switching.objects.filter(id=id).delete()
        return HttpResponse('delete post')


################
#蓄电池电源主机柜
################


#与数据库模型绑定的表单（蓄电池电源主机柜）
class Bjs_base_battery_power_mainframe_ModelForm(forms.ModelForm):
    class Meta:
        model = Bjs_base_battery_power_mainframe
        fields = '__all__'


#蓄电池电源主机柜（添加）
@login_required(login_url='/account/')
@permission_required(
    perm='home.add_bjs_base_battery_power_mainframe', login_url='/home/')
def add_bjs_base_battery_power_mainframe(request):
    if request.method == 'GET':
        BBBPMMF = Bjs_base_battery_power_mainframe_ModelForm()
        return render(request, 'add_bjs_base_battery_power_mainframe.html',
                      locals())
    else:
        BBBPMMF = Bjs_base_battery_power_mainframe_ModelForm(request.POST)
        if BBBPMMF.is_valid():
            BBBPMMF.save()
        return HttpResponse('add post')


#蓄电池电源主机柜（编辑）
@login_required(login_url='/account/')
@permission_required(
    perm='home.change_bjs_base_battery_power_mainframe', login_url='/home/')
def change_bjs_base_battery_power_mainframe(request):
    id = request.GET.get('id')
    obj = Bjs_base_battery_power_mainframe.objects.filter(id=id).first()
    if not obj:
        return HttpResponse('edit post not have obj')
    if request.method == 'GET':
        BBBPMMF = Bjs_base_battery_power_mainframe_ModelForm(instance=obj, )
        return render(request, 'change_bjs_base_battery_power_mainframe.html',
                      locals())
    else:
        BBBPMMF = Bjs_base_battery_power_mainframe_ModelForm(
            request.POST,
            instance=obj,
        )
        if BBBPMMF.is_valid():
            BBBPMMF.save()
        return HttpResponse('edit post')


#蓄电池电源主机柜（删除）
@login_required(login_url='/account/')
@permission_required(
    perm='home.delete_bjs_base_battery_power_mainframe', login_url='/home/')
def delete_bjs_base_battery_power_mainframe(request):
    id = request.GET.get('id')
    obj = Bjs_base_battery_power_mainframe.objects.filter(id=id).first()
    if not obj:
        return HttpResponse('delete post not have obj')
    if request.method == 'GET':
        BBBPMMF = Bjs_base_battery_power_mainframe_ModelForm(instance=obj, )
        return render(request, 'delete_bjs_base_battery_power_mainframe.html',
                      locals())
    else:
        Bjs_base_battery_power_mainframe.objects.filter(id=id).delete()
        return HttpResponse('delete post')


################
#分时下电柜
################


#与数据库模型绑定的表单（分时下电柜）
class Bjs_base_power_off_mainframe_ModelForm(forms.ModelForm):
    class Meta:
        model = Bjs_base_power_off_mainframe
        fields = '__all__'


#分时下电柜（添加）
@login_required(login_url='/account/')
@permission_required(
    perm='home.add_bjs_base_power_off_mainframe', login_url='/home/')
def add_bjs_base_power_off_mainframe(request):
    if request.method == 'GET':
        BBPOMMF = Bjs_base_power_off_mainframe_ModelForm()
        return render(request, 'add_bjs_base_power_off_mainframe.html',
                      locals())
    else:
        BBPOMMF = Bjs_base_power_off_mainframe_ModelForm(request.POST)
        if BBPOMMF.is_valid():
            BBPOMMF.save()
        return HttpResponse('add post')


#分时下电柜（编辑）
@login_required(login_url='/account/')
@permission_required(
    perm='home.change_bjs_base_power_off_mainframe', login_url='/home/')
def change_bjs_base_power_off_mainframe(request):
    id = request.GET.get('id')
    obj = Bjs_base_power_off_mainframe.objects.filter(id=id).first()
    if not obj:
        return HttpResponse('edit post not have obj')
    if request.method == 'GET':
        BBPOMMF = Bjs_base_power_off_mainframe_ModelForm(instance=obj, )
        return render(request, 'change_bjs_base_power_off_mainframe.html',
                      locals())
    else:
        BBPOMMF = Bjs_base_power_off_mainframe_ModelForm(
            request.POST,
            instance=obj,
        )
        if BBPOMMF.is_valid():
            BBPOMMF.save()
        return HttpResponse('edit post')


#分时下电柜（删除）
@login_required(login_url='/account/')
@permission_required(
    perm='home.delete_bjs_base_power_off_mainframe', login_url='/home/')
def delete_bjs_base_power_off_mainframe(request):
    id = request.GET.get('id')
    obj = Bjs_base_power_off_mainframe.objects.filter(id=id).first()
    if not obj:
        return HttpResponse('delete post not have obj')
    if request.method == 'GET':
        BBPOMMF = Bjs_base_power_off_mainframe_ModelForm(instance=obj, )
        return render(request, 'delete_bjs_base_power_off_mainframe.html',
                      locals())
    else:
        Bjs_base_power_off_mainframe.objects.filter(id=id).delete()
        return HttpResponse('delete post')


################
#电池柜
################


#与数据库模型绑定的表单（电池柜）
class Bjs_base_battery_mainframe_ModelForm(forms.ModelForm):
    class Meta:
        model = Bjs_base_battery_mainframe
        fields = '__all__'


#电池柜（添加）
@login_required(login_url='/account/')
@permission_required(
    perm='home.add_bjs_base_battery_mainframe', login_url='/home/')
def add_bjs_base_battery_mainframe(request):
    if request.method == 'GET':
        BBBMMF = Bjs_base_battery_mainframe_ModelForm()
        return render(request, 'add_bjs_base_battery_mainframe.html', locals())
    else:
        BBBMMF = Bjs_base_battery_mainframe_ModelForm(request.POST)
        if BBBMMF.is_valid():
            BBBMMF.save()
        return HttpResponse('add post')


#电池柜（编辑）
@login_required(login_url='/account/')
@permission_required(
    perm='home.change_bjs_base_battery_mainframe', login_url='/home/')
def change_bjs_base_battery_mainframe(request):
    id = request.GET.get('id')
    obj = Bjs_base_battery_mainframe.objects.filter(id=id).first()
    if not obj:
        return HttpResponse('edit post not have obj')
    if request.method == 'GET':
        BBBMMF = Bjs_base_battery_mainframe_ModelForm(instance=obj, )
        return render(request, 'change_bjs_base_battery_mainframe.html',
                      locals())
    else:
        BBBMMF = Bjs_base_battery_mainframe_ModelForm(
            request.POST,
            instance=obj,
        )
        if BBBMMF.is_valid():
            BBBMMF.save()
        return HttpResponse('edit post')


#电池柜（删除）
@login_required(login_url='/account/')
@permission_required(
    perm='home.delete_bjs_base_battery_mainframe', login_url='/home/')
def delete_bjs_base_battery_mainframe(request):
    id = request.GET.get('id')
    obj = Bjs_base_battery_mainframe.objects.filter(id=id).first()
    if not obj:
        return HttpResponse('delete post not have obj')
    if request.method == 'GET':
        BBBMMF = Bjs_base_battery_mainframe_ModelForm(instance=obj, )
        return render(request, 'delete_bjs_base_battery_mainframe.html',
                      locals())
    else:
        Bjs_base_battery_mainframe.objects.filter(id=id).delete()
        return HttpResponse('delete post')


################
#巡检记事
################


#与数据库模型绑定的表单（巡检记事）
class Bjs_base_other_situation_ModelForm(forms.ModelForm):
    class Meta:
        model = Bjs_base_other_situation
        fields = '__all__'


#巡检记事（添加）
@login_required(login_url='/account/')
@permission_required(
    perm='home.add_bjs_base_other_situation', login_url='/home/')
def add_bjs_base_other_situation(request):
    if request.method == 'GET':
        BBOSMF = Bjs_base_other_situation_ModelForm()
        return render(request, 'add_bjs_base_other_situation.html', locals())
    else:
        BBOSMF = Bjs_base_other_situation_ModelForm(request.POST)
        if BBOSMF.is_valid():
            BBOSMF.save()
        return HttpResponse('add post')


#巡检记事（编辑）
@login_required(login_url='/account/')
@permission_required(
    perm='home.change_bjs_base_other_situation', login_url='/home/')
def change_bjs_base_other_situation(request):
    id = request.GET.get('id')
    obj = Bjs_base_other_situation.objects.filter(id=id).first()
    if not obj:
        return HttpResponse('edit post not have obj')
    if request.method == 'GET':
        BBOSMF = Bjs_base_other_situation_ModelForm(instance=obj, )
        return render(request, 'change_bjs_base_other_situation.html',
                      locals())
    else:
        BBOSMF = Bjs_base_other_situation_ModelForm(
            request.POST,
            instance=obj,
        )
        if BBOSMF.is_valid():
            BBOSMF.save()
        return HttpResponse('edit post')


#巡检记事（删除）
@login_required(login_url='/account/')
@permission_required(
    perm='home.delete_bjs_base_other_situation', login_url='/home/')
def delete_bjs_base_other_situation(request):
    id = request.GET.get('id')
    obj = Bjs_base_other_situation.objects.filter(id=id).first()
    if not obj:
        return HttpResponse('delete post not have obj')
    if request.method == 'GET':
        BBOSMF = Bjs_base_other_situation_ModelForm(instance=obj, )
        return render(request, 'delete_bjs_base_other_situation.html',
                      locals())
    else:
        Bjs_base_other_situation.objects.filter(id=id).delete()
        return HttpResponse('delete post')