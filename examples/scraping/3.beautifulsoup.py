from bs4 import BeautifulSoup
from urllib.request import urlopen

# 打开网页，读出网页的全部内容，并用utf-8的编码形式
html = urlopen(
    'https://morvanzhou.github.io/static/scraping/list.html'
).read().decode('utf-8')
print(html)

# 用lxml的方式解析网页代码
soup = BeautifulSoup(html, features='lxml')
# 使用class来解析网页代码
month = soup.find_all('li', {'class': 'month'})
for m in month:
    print(m.get_text())  # 读出li中包含month类的所有文本


# 用find找出ul中包含class=jan的内容，注意find和find_all的区别
# find为文本，find_all为数组
jan = soup.find('ul', {'class': 'jan'})
print(jan)

jan_text = jan.find_all('li')
print(jan_text)
for j in jan_text:
    print(j.get_text())  # get_text取出标签中的文本
