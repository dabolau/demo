import pandas as pd
import numpy as np

# 生成日期数据从20180101-20180106
dates = pd.date_range('20180101', periods=6)
# 生成0-23的矩阵，左边标题为日期数据20180101-20180106，上边标题为A，B，C，D
df = pd.DataFrame(np.arange(24).reshape((6, 4)),
                  index=dates, columns=['A', 'B', 'C', 'D'])


print(df)
df.iloc[0, 1] = np.nan  # 设置0行1列设置为NaN
df.iloc[1, 2] = np.nan  # 设置1行2列设置为NaN
print(df)

# how={'any','all'}any表示这一行只要有Nan就丢掉all表示这一行全部都是NaN才丢掉
# print(df.dropna(axis=0, how='any'))   #axis=0表示行，axis=1表示列
# print(df.fillna(value=0))  # 填充内容
print(df.isnull())  # 查看是否有缺失数据
print(np.any(df.isnull()) == True)  # 查看是否有一个是Ture的数据
