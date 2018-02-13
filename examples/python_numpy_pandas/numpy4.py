import numpy as np
# 创建一个数值2-14的3行4列的矩阵
A = np.arange(14, 2, -1).reshape(3, 4)

print(A)
print(np.argmin(A))  # 获取矩阵中的最小值的索引
print(np.argmax(A))  # 获取矩阵中的最大值的索引
print(np.mean(A))  # 获取矩阵中的平均数
print(A.mean())  # 获取矩阵中的平均数
print(np.median(A))  # 获取矩阵中的中位数
print(np.cumsum(A))  # 累加矩阵中的值
print(np.diff(A))  # 累差矩阵中的值
print(np.nonzero(A))  # 获取非零的数，输出的值是多少行多少列
print(np.sort(A))  # 排序为
print(np.transpose(A))  # 倒过来，行列对倒
print((A.T).dot(A))  # 矩阵乘法
print(np.clip(A, 5, 9))  # 小于5的数替换为5，大于9的数替换为9
print(np.mean(A, axis=0))  # 所有的都有这个参数，axis=0表示列，axis=1表示行
