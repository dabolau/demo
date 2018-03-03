# 批量裁剪自定义图片
from PIL import Image
import random
import os


# 获取目录中的所有目录和文件
def get_file_list(dir, file_list):
    new_dir = dir
    if os.path.isfile(dir):
        file_list.append(dir)
    elif os.path.isdir(dir):
        for d in os.listdir(dir):
            new_dir = os.path.join(dir, d)
            get_file_list(new_dir, file_list)
    return file_list


if __name__ == '__main__':
    # 定义图片裁剪大小位置
    up = int(input('上：'))
    down = int(input('下：'))
    left = int(input('左：'))
    right = int(input('右：'))
    # 目录位置
    get_file_dir = 'image'
    # 所有文件列表
    list = get_file_list(get_file_dir, [])
    # 循环处理图片
    for l in list:
        print('路径：' + l)
        # 打开图片
        img = Image.open(l)
        # 设置图片裁剪尺寸（左上右下）
        box = (left, up, right, down)
        # 裁剪区域
        region = img.crop(box)
        # 保存图片
        region.save(
            os.path.splitext(l)[0] + '_' + str(random.randint(1000, 9000)) +
            '.jpg')
        # 打印图片信息
        print('原图：' + str(img.size[0]) + 'x' + str(img.size[1]) +
              '，裁剪：' + str(down - up) + 'x' + str(right - left))
