import requests

# 网页地址，POST处理的网址
# http://pythonscraping.com/files/form2.html
url = 'http://pythonscraping.com/files/processing2.php'
# 打开文件写到缓存中
upfile = {'uploadFile': open('./img/upload_image.jpg', 'rb')}
# 提交文件到url中的地址里进行上传
req = requests.post(url, files=upfile)
# 打印网页内容
print(req.text)
