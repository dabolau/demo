from bs4 import BeautifulSoup
import requests
import os

# 创建img文件夹
os.makedirs('./img/', exist_ok=True)
# 国家地理每日一图地址
base_url = 'http://www.nationalgeographic.com.cn/photography/photo_of_the_day/'
# 用get形式获取网页内容
html = requests.get(base_url).text
# 用lxml解析器解析网页文本
soup = BeautifulSoup(html, features='lxml')
# 找出所有a标签中属性为class="imgs"的内容
img_url = soup.find_all('a', attrs={'class': 'imgs'})
# 在找出的内容中又包含img标签
for ul in img_url:
    # 找出所有img标签中的内容
    imgs = ul.find_all('img')
    # 在找出img标签中的src属性的内容
    for img in imgs:
        # 找出图片的地址
        url = img['src']
        # 分割图片地址，获取/末尾内容
        img_name = url.split('/')[-1]
        # 打开图片网址，用stream=True的形式
        r = requests.get(url, stream=True)
        # 用文本流的形式保存到文件
        with open('./img/' + img_name, mode='wb') as f:
            for chunk in r.iter_content(chunk_size=32):
                f.write(chunk)
        # 打印出下载内容的名字
        print('download: %s' % img_name)
