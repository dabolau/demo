import os
import requests

# 在当前目录创建img文件夹
os.makedirs('./img/', exist_ok=True)
# 图片地址
img_url = 'https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'
# 用get形式打开图片地址
r = requests.get(img_url)
# 将图片内容写入到文件
with open('./img/requests_image.png', 'wb') as f:
    f.write(r.content)
