from urllib.request import urlopen
import re

html = urlopen(
    'https://morvanzhou.github.io/static/scraping/basic-structure.html'
).read().decode('utf-8')
print(html)

# 选择标题
# res = re.findall(r'<title>(.+?)</title>',html)
# print('\npage title is: ', res[0])

# 选择段，并多行的形式
# res = re.findall(r'<p>(.+?)</p>',html,flags=re.DOTALL)
# print('\npage paragraph is: ', res[0])

# 选择超链接
res = re.findall(r'href="(.+?)"', html)
print('\nlinks is: ', res)
