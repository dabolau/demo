from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# 打开网页，读出网页的全部内容，并用utf-8的编码形式
html = urlopen(
    'https://morvanzhou.github.io/static/scraping/table.html'
).read().decode('utf-8')
print(html)

# 用lxml的方式解析网页代码
soup = BeautifulSoup(html, features='lxml')

# 找出带.jpg后缀的网页链接，找出img标签，找到src属性
img_links = soup.find_all('img', attrs={'src': re.compile('.*?\.jpg')})
for link in img_links:
    print(link['src'])

print('###')

# 找出所有a标签中属性为href的链接
course_links = soup.find_all(
    'a', attrs={'href': re.compile('https://morvanzhou.*')})
for link in course_links:
    print(link['href'])
