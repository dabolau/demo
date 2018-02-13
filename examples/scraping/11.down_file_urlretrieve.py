import os
from urllib.request import urlretrieve

# 在当前目录创建img文件夹
os.makedirs('./img/', exist_ok=True)
# 图片地址
img_url = 'https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'
# 用urlretrieve下载图片
urlretrieve(img_url, filename='./img/urlretrieve_image.png')
