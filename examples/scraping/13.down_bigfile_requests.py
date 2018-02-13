import os
import requests

# 在当前目录创建img文件夹
os.makedirs('./img/', exist_ok=True)
# 图片地址
img_url = 'https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'
# 用get形式打开图片地址，下载大文件需要用到stream=True
r = requests.get(img_url, stream=True)
# 将图片内容写入到文件
with open('./img/requests_big_image.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)
