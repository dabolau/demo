from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image
import qrcode
import zbarlight
import uuid


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


###
# 生成二维码
###
def home(request):
    if request.method == 'GET':
        message = ''
        return render(request, 'home.html', locals())
    if request.method == 'POST':
        text = request.POST.get('text')
        if text == '':
            message = '你没有输入任何内容'
        else:
            # 生成二维码
            qr = qrcode.make(text)
            u = str(uuid.uuid1())
            # 保存生成的二维码为图片
            qr.save('home/static/qr/' + u + '.png')
            p = 'download/qr/' + u + '.png'
            message = ''
    return render(request, 'home.html', locals())


###
# 扫描二维码
###
def scan(request):
    if request.method == 'GET':
        message = ''
        return render(request, 'scan.html', locals())
    if request.method == 'POST':
        upfile = request.FILES.get('upfile', '')
        if upfile == '':
            message = '你没有选择任何文件'
        else:
            u = str(uuid.uuid1())
            # 打开特定的文件进行二进制的写操作
            destination = open('home/static/qr/' + u + '.png', 'wb+')
            # 分块写入文件
            for chunk in upfile.chunks():
                destination.write(chunk)
            # 关闭文件
            destination.close()
            # 二维码上传后的新路径
            file_path = 'home/static/qr/' + u + '.png'
            # 打开并读取二维码图片
            with open(file_path, 'rb') as qr_file:
                qr = Image.open(qr_file)
                qr.load()
            # 扫描二维码文件获得二维码中的内容
            qr_content = zbarlight.scan_codes('qrcode', qr)
            # 获得二维码文件路径
            p = 'download/qr/' + u + '.png'
            if qr_content == None:
                message = '扫描二维码内容失败'
            else:
                message = str(qr_content[0].decode('utf-8'))
    return render(request, 'scan.html', locals())
