import pandas as pd
import numpy as np

# 合并三组数据
# df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
# df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
# df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])
# print(df1)
# print(df2)
# print(df3)

# #竖着合并，用ignore_index=True重新排序
# res = pd.concat([df1, df2, df3], axis=0,ignore_index=True)  # axis=0表示竖着,axis=0表示横着
# print(res)


# df1 = pd.DataFrame(np.ones((3, 4)) * 0,
#                    index=[1, 2, 3], columns=['a', 'b', 'c', 'd'])
# df2 = pd.DataFrame(np.ones((3, 4)) * 1,
#                    index=[2, 3, 4], columns=['b', 'c', 'd', 'e'])
# print(df1)
# print(df2)

# # 默认情况下是用的join='outer'合并后，没有的会自动用NaN填充
# # join='inner'是只处理有数据的部分，其他的就排除掉
# res = pd.concat([df1, df2], join='inner', ignore_index=True)

# print(res)


# df1 = pd.DataFrame(np.ones((3, 4)) * 0,
#                    index=[1, 2, 3], columns=['a', 'b', 'c', 'd'])
# df2 = pd.DataFrame(np.ones((3, 4)) * 1,
#                    index=[2, 3, 4], columns=['b', 'c', 'd', 'e'])
# print(df1)
# print(df2)

# #join_axes=[df1.index]只有有的数据会填充，默认情况下是全部填充
# res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
# print(res)


# df1 = pd.DataFrame(np.ones((3, 4)) * 0,
#                    columns=['a', 'b', 'c', 'd'])
# df2 = pd.DataFrame(np.ones((3, 4)) * 1,
#                    columns=['a', 'b', 'c', 'd'])
# df3 = pd.DataFrame(np.ones((3, 4)) * 1,
#                    columns=['a', 'b', 'c', 'd'])

# print(df1)
# print(df2)

# #把数据加入到df1中并重新排序
# res = df1.append([df2, df3], ignore_index=True)

# print(res)


df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(df1)
print(s1)

# 一行一行的添加数据
res = df1.append(s1, ignore_index=True)
print(res)
