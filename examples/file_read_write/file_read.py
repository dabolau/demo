# 打开文件myfile.txt，‘r’表示只读方式打开文件，默认在文件开头
my_file = open('myfile.txt', 'r')
# 将文件内容存放到变量text中
text = my_file.readline()
# 关闭文件
my_file.close()
# 打印文件
print(text)
