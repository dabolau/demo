text = 'line1\nline2\nline3'

# 打开文件myfile.txt，‘w’表示打开并写入文件，文件不存在，创建新文件
my_file = open('myfile.txt', 'w')
# 将text内的内容写入到文件
my_file.write(text)
# 关闭文件
my_file.close()
