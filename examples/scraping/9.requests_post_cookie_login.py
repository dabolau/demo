import requests

# 网页地址，POST处理的网址
# http://pythonscraping.com/pages/cookies/login.html
url = 'http://pythonscraping.com/pages/cookies/welcome.php'
url2 = 'http://pythonscraping.com/pages/cookies/profile.php'
# 要提交数据
data = {'username': 'db', 'password': 'password'}
# 用post形式提交数据
req = requests.post(url, data=data)
# 打印出post请求后的cookies
print(req.cookies.get_dict())
# 用post形式带上cookies提交数据
req = requests.get(url2, cookies=req.cookies)
# 打印网页内容
print(req.text)
