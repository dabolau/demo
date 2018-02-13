import pandas as pd


# http://pandas.pydata.org/pandas-docs/stable/io.html
# 读写文件的操作
data = pd.read_csv('students.csv')  # 读出students.csv文件中的数据
print(data)
data.to_excel('1.xls')  # 保存到文件，以xls格式
