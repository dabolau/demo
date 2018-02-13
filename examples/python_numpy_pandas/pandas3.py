import pandas as pd
import numpy as np

# 生成日期数据从20180101-20180106
dates = pd.date_range('20180101', periods=6)
# 生成0-23的矩阵，左边标题为日期数据20180101-20180106，上边标题为A，B，C，D
df = pd.DataFrame(np.arange(24).reshape((6, 4)),
                  index=dates, columns=['A', 'B', 'C', 'D'])

print(df)
df.iloc[2, 2] = 1111  # 用索引的方式修改第二行第二列的值
df.loc['20180101', 'B'] = 2222  # 用标签的方式修改20180101和B的值
# df[df.A > 4] = 0 # 用df直接将df中A列后面的所有大于4的内容等于0（包括B，C，D也一起修改）
df.A[df.A > 4] = 0  # 用df.A列中只有A后面大于4的内容等于0
df['E'] = np.nan  # 添加F这一列
df['F'] = pd.Series([1, 2, 3, 4, 5, 6],
                    index=pd.date_range('20180101', periods=6))  # 在20180101-20180106的F这列添加1，2，3，4，5，6
print(df)
