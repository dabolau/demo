append_text = '\nappend text'


# 使用with as方法打开文件不用使用f.close关闭文件
with open('with_myfile.txt', 'a') as f:
    f.write(append_text)
