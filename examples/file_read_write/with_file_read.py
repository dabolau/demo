# 使用with as方法打开文件不用使用f.close关闭文件
with open('with_myfile.txt', 'r') as f:
    text = f.readline()
print(text)
