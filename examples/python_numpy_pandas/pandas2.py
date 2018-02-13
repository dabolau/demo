import pandas as pd
import numpy as np

# 生成日期数据从20180101-20180106
dates = pd.date_range('20180101', periods=6)
# 生成0-23的矩阵，左边标题为日期数据20180101-20180106，上边标题为A，B，C，D
df = pd.DataFrame(np.arange(24).reshape((6, 4)),
                  index=dates, columns=['A', 'B', 'C', 'D'])

print(df['A'])  # 选择A序列
print(df.A)  # 选择A序列
print(df[0:3])  # 选择日期序列
print(df['20180102':'20180104'])  # 选择日期序列

# loc标签选择
print(df.loc['20180102'])  # 标签选择
print(df.loc[:, ['A', 'B']])  # 标签选择
print(df.loc['20180102', ['A', 'B']])  # 标签具体选择

# iloc索引选择
print(df.iloc[3])  # 选择第三行
print(df.iloc[3, 1])  # 选择第三行第一位
print(df.iloc[3:5, 1:3])  # 选择第三行到第五行第一位到第三位
print(df.iloc[[1, 3, 5], 1:3])  # 选择第一三五行第一到三位

# ix是标签和索引的合并选择
print(df.ix[:3, ['A', 'C']])  # 选择第零到三行A，B的内容

# 是和否的选择
print(df)
print(df[df.A > 8])
print(df[df.A < 8])