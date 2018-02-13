text = '111\n222\n333'


# 使用with as方法打开文件不用使用f.close关闭文件
with open('with_myfile.txt', 'w') as f:
    f.write(text)
