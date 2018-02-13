append_text = '\nappend text'

# 打开文件myfile.txt，‘a’表示打开并追加写入文件，文件不存在，创建新文件
my_file = open('myfile.txt', 'a')
# 将append_text内的内容追加写入到文件myfile.txt的最后面
my_file.write(append_text)
# 关闭文件
my_file.close()
