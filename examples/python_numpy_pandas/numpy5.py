import numpy as np

# 创建数组
A = np.arange(3, 15)
# 获取索引
print(A[3])

# 创建矩阵
B = np.arange(3, 15).reshape((3, 4))
print(B)
# 获取具体索引
print(B[1, 1])
print(B[2][1])
print(B[1, :])
print(B[:, 0])
print(B[1, 2:3])

# 迭代所有行
for row in B:
    print(row)

# 迭代所有列
for column in B.T:
    print(column)

# 迭代所有项
for item in B.flat:
    print(item)

# 将矩阵转换为一维数组
print(A.flatten())
