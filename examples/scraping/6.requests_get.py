import requests
import webbrowser

# 百度网址
base_url = 'https://www.baidu.com/s'
# 参数
param = {'wd': '莫烦python'}
# 用requests.get方法打开带参数的百度网址
req = requests.get(base_url, params=param)
print(req.url)
# 用系统自带浏览器打开网址
webbrowser.open(req.url)
