import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 在当前目录创建img文件夹
os.makedirs('./img/', exist_ok=True)
# 创建选项
chrome_options = Options()
# 定义无头
chrome_options.add_argument('--headless')
# 使用Chromedriver驱动，并设置选项
driver = webdriver.Chrome(chrome_options=chrome_options)
# 打开网站
driver.get("https://morvanzhou.github.io/")
# 按顺序点击网站
driver.find_element_by_link_text(u"赞助").click()
driver.find_element_by_link_text("About").click()
driver.find_element_by_link_text(u"教程 ▾").click()
driver.find_element_by_link_text(u"推荐学习顺序").click()
# 获取网页源代码
html = driver.page_source
# 保存截屏为文件
driver.get_screenshot_as_file('./img/sreenshot.png')
# 关闭
driver.close()
print(html)
