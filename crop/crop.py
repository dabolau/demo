# coding=utf-8

#批量裁剪自定义图片
from PIL import Image
import random
import sys
import os

#设置默认编码utf-8
reload(sys)
sys.setdefaultencoding('utf-8')


#获取目录中的所有目录和文件
def get_file_list(dir, file_list):
    new_dir = dir
    if os.path.isfile(dir):
        file_list.append(dir.decode('gbk'))
    elif os.path.isdir(dir):
        for d in os.listdir(dir):
            new_dir = os.path.join(dir, d)
            get_file_list(new_dir, file_list)
    return file_list


#目录位置
get_file_dir = 'crop'
#所有文件列表
list = get_file_list(get_file_dir, [])
#循环处理图片
for l in list:
    print l
    #打开图片
    img = Image.open(l)
    #设置图片裁剪尺寸
    box = (img.size[0] - 420, 0, img.size[0], img.size[1])
    #裁剪区域
    region = img.crop(box)
    #保存图片
    region.save(
        os.path.splitext(l)[0] + '_' + str(random.randint(1000, 9000)) +
        '.jpg')
    #打印图片信息
    print 'old_x, old_y：' + str(
        img.size[0]) + '|' + str(img.size[1]) + ', new_x, new_y：' + str(
            img.size[0] - (img.size[0] - 420)) + '|' + str(img.size[1])
