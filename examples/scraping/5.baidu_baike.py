from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

# 百度百科基础地址
base_url = 'https://baike.baidu.com'
# 百度百科的关键词
his = ['/item/%E4%BA%92%E8%81%94%E7%BD%91']

for i in range(10):
    # 组合成完整的地址，[-1]表示从列表的末尾取出一条数据
    url = base_url + his[-1]
    # 打开百度百科的地址，以utf-8读出网页代码
    html = urlopen(url).read().decode('utf-8')
    # 用BeautifulSoup中的lxml解析器解析网页
    soup = BeautifulSoup(html, features='lxml')
    # 打印出第一个h1标签中的文本内容和网址
    print(soup.find('h1').get_text(), his[-1])
    # 找出所有a标签中属性为target="_blank"的网页地址
    sub_urls = soup.find_all('a', attrs={
        'target': '_blank',
        'href': re.compile('/item/(%.{2})+$')})
    # 如果读出sub_urls列表中的地址不为空
    if len(sub_urls) != 0:
        # 提取出sub_urls列表中的一个随机地址，加入到his列表中
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        # 如果读出sub_urls为空，清除内容。
        his.pop()
