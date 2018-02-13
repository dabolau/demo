import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1])  # 生成一个带索引的列表
print(s)
dates = pd.date_range('20180122', periods=6)  # 生成一个日期格式的列表
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates,
                  columns=['a', 'b', 'c', 'd'])  # 其中index定义的行索引，columns定义的列索引，类似表格
print(df)
df1 = pd.DataFrame(np.arange(12).reshape(3, 4))  # 默认情况下行列分别为0，1，2.。。。的方式生成索引
print(df1)
df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20180122'), 'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'), 'E': pd.Categorical(['test', 'train', 'test', 'train']), 'F': 'foo'})
print(df2)
print(df2.dtypes)  # 类型
print(df2.index)  # 行索引
print(df2.columns)  # 列索引
print(df2.values)  # 值
print(df2.describe())
print(df2.T)  # 数据横纵颠倒
print(df2.sort_index(axis=1, ascending=False))  # 以到序列的横向排序
print(df2.sort_index(axis=0, ascending=False))  # 以到序列的纵向排序
print(df2.sort_values(by='E'))  # 以值来排序
