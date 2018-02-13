import pandas as pd
import numpy as np


# #定义资料集并打印出
# left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                              'A': ['A0', 'A1', 'A2', 'A3'],
#                              'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                               'C': ['C0', 'C1', 'C2', 'C3'],
#                               'D': ['D0', 'D1', 'D2', 'D3']})

# print(left)
# print(right)


# #以key为中心合并数据到左右
# res = pd.merge(left, right, on='key')
# print(res)


#


# #定义资料集并打印出
# df1 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})
# df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})
# print(df1)
# print(df2)

# # 依据col1进行合并，并启用indicator=True，最后打印出
# res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
# print(res)

# # 自定indicator column的名称，并打印出
# res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')
# print(res)



# #定义资料集并打印出
# left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
#                      'B': ['B0', 'B1', 'B2']},
#                      index=['K0', 'K1', 'K2'])
# right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
#                       'D': ['D0', 'D2', 'D3']},
#                      index=['K0', 'K2', 'K3'])

# print(left)
# print(right)

# #依据左右资料集的index进行合并，how='outer',并打印出
# res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
# print(res)

# #依据左右资料集的index进行合并，how='inner',并打印出
# res = pd.merge(left, right, left_index=True, right_index=True, how='inner')
# print(res)


#定义资料集
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
print(boys)
print(girls)

#使用suffixes解决overlapping的问题
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='outer')
print(res)
