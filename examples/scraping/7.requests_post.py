import requests

# 网页地址，POST处理的网址
# http://pythonscraping.com/files/form.html
url = 'http://pythonscraping.com/pages/files/processing.php'
# 要提交的数据
data = {'firstname': 'db', 'lastname': 'lee'}
# 打开网址
req = requests.post(url, data=data)
# 打印网页内容
print(req.text)
