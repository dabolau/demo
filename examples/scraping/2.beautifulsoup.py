from bs4 import BeautifulSoup
from urllib.request import urlopen

# 打开网页，读出网页的全部内容，并用utf-8的编码形式
html = urlopen(
    'https://morvanzhou.github.io/static/scraping/basic-structure.html'
).read().decode('utf-8')
print(html)

# 用lxml的方式解析网页代码
soup = BeautifulSoup(html, features='lxml')
print(soup.h1, '\n')  # 读出h1中的内容和标签
print(soup.p, '\n')  # 读出p中的内容和标签
print('######')

all_href = soup.find_all('a')
for href in all_href:
    print(href['href'])  # 只读出href中的内容
