from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import qrcode
import uuid


###
# 视图首页
###
def home(request):
    if request.method == 'GET':
        error = ''
        return render(request, 'home.html', locals())
    if request.method == 'POST':
        text = request.POST.get('text')
        if text == '':
            error = '你没有输入任何内容'
        else:
            qr = qrcode.make(text)
            u = str(uuid.uuid1())
            qr.save('home/static/qr/' + u + '.png')
            p = 'download/qr/' + u + '.png'
            error = ''
    return render(request, 'home.html', locals())


###
# 404页面，开启需要将配置修改为（DEBUG=False）
###
def page_not_found(request):
    return render(request, '404.html', locals())


###
# 500页面，开启需要将配置修改为（DEBUG=False）
###
def page_error(request):
    return render(request, '500.html', locals())